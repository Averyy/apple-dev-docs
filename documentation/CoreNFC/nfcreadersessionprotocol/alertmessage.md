# alertMessage

**Framework**: Core NFC  
**Kind**: property  
**Required**: Yes

A custom description that helps users understand how they can use NFC reader mode in your app.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var alertMessage: String { get set }
```

#### Discussion

Before you call [`begin()`](nfcreadersessionprotocol/begin().md), use this property to supply a string that provides more context about how your app uses NFC reader mode. For example, you might tell users “Hold your iPhone near the item to learn more about it.” When tag scanning begins, your text is displayed to users in an alert. Note that the [`alertMessage`](nfcreadersessionprotocol/alertmessage.md) string is different from the purpose string you supply for the [`NFCReaderUsageDescription`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/uid/TP40009251-SW74) key in your `Info.plist` file.

If you configure your NFC NDEF reader session to read multiple tags, you can update [`alertMessage`](nfcreadersessionprotocol/alertmessage.md) to display different information after each tag is read (you can update this string in any thread context while the reader session remains valid).

## See Also

- [func begin()](nfcreadersessionprotocol/begin.md)
  Starts the reader session.
- [func invalidate()](nfcreadersessionprotocol/invalidate.md)
  Closes the reader session, which prevents it from being reused.
- [func invalidate(errorMessage: String)](nfcreadersessionprotocol/invalidate(errormessage:).md)
  Closes the reader session and displays an error message to the user.
- [func begin()](nfcreadersessionprotocol/begin.md)
  Starts the reader session.
- [func invalidate()](nfcreadersessionprotocol/invalidate.md)
  Closes the reader session, which prevents it from being reused.
- [func invalidate(errorMessage: String)](nfcreadersessionprotocol/invalidate(errormessage:).md)
  Closes the reader session and displays an error message to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcreadersessionprotocol/alertmessage)*