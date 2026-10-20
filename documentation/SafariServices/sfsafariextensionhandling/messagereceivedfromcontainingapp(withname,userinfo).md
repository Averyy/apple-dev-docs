# messageReceivedFromContainingApp(withName:userInfo:)

**Framework**: Safari Services  
**Kind**: method  
**Role**: Instance Method

A method the system calls when the extension receives a message from the extension’s containing app.

**Availability**:
- macOS 10.12.4+

## Declaration

```swift
optional func messageReceivedFromContainingApp(withName messageName: String, userInfo: [String : Any]? = nil)
```

```objc
- (void) messageReceivedFromContainingAppWithName:(NSString *) messageName userInfo:(NSDictionary<NSString *,id> *) userInfo;
```

## Parameters

- `messageName`: A string that identifies the message.
- `userInfo`: Optional message content.

## See Also

### Related Documentation
- [class func dispatchMessage(withName: String, toExtensionWithIdentifier: String, userInfo: [String : Any]?, completionHandler: (((any Error)?) -> Void)?)](../sfsafariapplication/dispatchmessage%28withname,toextensionwithidentifier,userinfo,completionhandler%29.md)
  Sends a message to a Safari app extension, launching Safari if necessary.
### Receiving Messages in Your App Extension
- [func messageReceived(withName: String, from: SFSafariPage, userInfo: [String : Any]?)](./messagereceived%28withname,from,userinfo%29.md)
  A method the system calls when the extension receives a message from an injected script.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sfsafariextensionhandling/messagereceivedfromcontainingapp(withname:userinfo:))*