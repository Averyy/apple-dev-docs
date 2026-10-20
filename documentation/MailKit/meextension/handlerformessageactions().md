# handlerForMessageActions()

**Framework**: MailKit  
**Kind**: method  
**Role**: Instance Method

Returns an object that performs actions on mail messages as the system downloads them.

**Availability**:
- macOS 12.0+

## Declaration

```swift
optional func handlerForMessageActions() -> any MEMessageActionHandler
```

```objc
- (id<MEMessageActionHandler>) handlerForMessageActions;
```

#### Return Value

An object that performs actions on mail messages.

#### Discussion

> 💡 **Tip**:  Message action handlers typically don’t need any additional state to determine the actions to take on messages. Therefore, using a singleton handler instance is appropriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/meextension/handlerformessageactions())*