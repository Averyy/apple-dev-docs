# TN3189: Managing Mail background traffic load

**Framework**: Technotes

Identify iOS Mail background traffic and manage its impact on your IMAP server.

#### Overview

To enhance the user experience, iOS Mail downloads a user’s email in the background. As part of a software update, some email data may require re-downloading. Since many devices will update at similar times, iOS Mail introduces a mechanism for IMAP email servers to limit concurrent downloads.

This process involves two main steps:

1. **Client identification:** [`RFC 3501`](https://developer.apple.comhttps://tools.ietf.org/html/rfc3501) IMAP email servers can detect if a connection is for a background download. iOS Mail clients identify themselves to the server using the `ID` command. Starting with iOS 18.5, this command includes an `event` field. This field will indicate if the connection is being used for background downloading.
2. **Load shedding:** If the server needs to limit its load and the client has been identified as a background download, the server should send a `NO [UNAVAILABLE]` tagged response to the `ID` command. This will result in the background download being postponed approximately a day, after which the client will retry the download.

#### Identify Background Traffic From Mail

Starting with iOS 18.5, the [`RFC 2971`](https://developer.apple.comhttps://tools.ietf.org/html/rfc2971) `ID` command includes an `event` field. The value of this field is either `NIL` or a list of comma-separated identifiers.

The server should only consider the `event` field value if the email client identifies itself with a `name` field that has a `com.apple.` prefix. For example, `"name" "com.apple.email.maild"` indicates that this is the the Mail app.

If the comma-separated identifiers of the `event` field include either:

- `indexer`, or
- `back-fill`,

it indicates that the connection is being used for background downloading.

> **Note**: The event field may contain other identifiers, either by themselves or as a list of comma-separated identifiers. The server should ignore all identifiers except `indexer` and `back-fill`. Allowing for other identifiers supports extension without affecting IMAP email servers’ ability to detect background downloading.

The `event` field could take on values such as:

- `periodic`
- `periodic,push`
- `NIL`

These would *not* indicate a background download. However, values such as:

- `back-fill`
- `periodic,back-fill`
- `back-fill,periodic`
- `indexer`

would indicate background download activity because they include `indexer` or `back-fill`.

Here’s an example interaction between the client (C) and server (S):

```None
C: A1 ID ("name" "com.apple.email.maild" "os" "iOS" "vendor" "Apple Inc" "event" NIL)
S: * ID ("name" "Mail Server" "version" "3")
S: A1 OK Completed
```

In this example, the client did include the `event` field, but its value is `NIL`. This is not a background download.

Here’s another example interaction:

```text
C: A1 ID ("name" "com.apple.email.search-indexer" "os" "iOS" "vendor" "Apple Inc" "event" "indexer")
S: * ID ("name" "Mail Server" "version" "3")
S: A1 OK Completed
```

In this case, the client indicated that it is performing a background download through the `indexer` value of the `event` field.

#### Tell Mail to Back Off

Since iOS Mail may use an already established connection to perform background activity, iOS Mail might send subsequent `ID` commands with updated `event` fields. These will always contain the full set of fields of the original `ID` command, notably the `name` and `event` field. These subsequent `ID` commands may include switching from non-background to background download.

The load shedding using `NO [UNAVAILABLE]` for background downloads lets IMAP email servers reduce peak load without a direct impact on user experience.

IMAP email servers should only send `NO [UNAVAILABLE]` when the Mail app has identified itself as Mail through the `name` field, and has indicated that it is doing background downloads through the `event` field as noted above.

Here’s an example of an interaction where the IMAP email server tell the Mail app to back off:

```text
C: A1 ID ("name" "com.apple.email.maild" "os" "iOS" "vendor" "Apple Inc" "event" "back-fill,periodic")
S: * ID ("name" "Mail Server" "version" "3")
S: A1 NO [UNAVAILABLE] Completed
```

Here the IMAP email server responds with a tagged response containing `NO` and the response code `UNAVAILABLE,` as defined in [`RFC 3501`](https://developer.apple.comhttps://tools.ietf.org/html/rfc3501) and [`RFC 5530`](https://developer.apple.comhttps://tools.ietf.org/html/rfc5530). This informs the iOS Mail app to back off, and it will close the connection.

> **Note**: Mail does not include an event field on macOS. It also doesn’t handle load shedding through the `NO [UNAVAILABLE]` server response.

#### Revision History

- **2025-05-09** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3189-managing-mail-background-traffic-load)*