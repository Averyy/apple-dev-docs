# messageReceived(withName:from:userInfo:)

**Framework**: Safari Services  
**Kind**: method

A method the system calls when the extension receives a message from an injected script.

**Availability**:
- macOS 10.12+

## Declaration

```swift
optional func messageReceived(withName messageName: String, from page: SFSafariPage, userInfo: [String : Any]? = nil)
```

## Mentions

- [Passing messages between Safari app extensions and injected scripts](passing-messages-between-safari-app-extensions-and-injected-scripts.md)

## Parameters

- `messageName`: A string that identifies the message.
- `page`: The page that sent the message.
- `userInfo`: Optional message content. If specified, the dictionary’s value objects conform to the W3C standard for safe passing of structured data, such as Boolean objects, numeric values, strings, and arrays.

## See Also

- [func messageReceivedFromContainingApp(withName: String, userInfo: [String : Any]?)](sfsafariextensionhandling/messagereceivedfromcontainingapp(withname:userinfo:).md)
  A method the system calls when the extension receives a message from the extension’s containing app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/messagereceived(withname:from:userinfo:))*