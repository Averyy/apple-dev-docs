# init()

**Framework**: Messages  
**Kind**: init  
**Role**: Initializer

Initializes a new message that is not part of a session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+

## Declaration

```swift
init()
```

```objc
- (instancetype) init;
```

#### Return Value

A newly initialized message.

#### Discussion

Use this initializer to create a new message that transmits app data, but is not updatable. When the recipient selects the message, the recipient’s app extension launches and receives the message object, but it cannot update the message.

## See Also

### Creating Messages
- [init(session: MSSession)](./init%28session%29.md)
  Initializes a new message that is part of the provided session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessage/init())*