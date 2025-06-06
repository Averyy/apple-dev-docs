# messageReceivedFromContainingApp(withName:userInfo:)

**Framework**: Safari Services  
**Kind**: method

A method the system calls when the extension receives a message from the extension’s containing app.

**Availability**:
- macOS 10.12.4+

## Declaration

```swift
optional func messageReceivedFromContainingApp(withName messageName: String, userInfo: [String : Any]? = nil)
```

## Parameters

- `messageName`: A string that identifies the message.
- `userInfo`: Optional message content.

## See Also

- [class func dispatchMessage(withName: String, toExtensionWithIdentifier: String, userInfo: [String : Any]?, completionHandler: (((any Error)?) -> Void)?)](sfsafariapplication/dispatchmessage(withname:toextensionwithidentifier:userinfo:completionhandler:).md)
  Sends a message to a Safari app extension, launching Safari if necessary.
- [func messageReceived(withName: String, from: SFSafariPage, userInfo: [String : Any]?)](sfsafariextensionhandling/messagereceived(withname:from:userinfo:).md)
  A method the system calls when the extension receives a message from an injected script.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/messagereceivedfromcontainingapp(withname:userinfo:))*