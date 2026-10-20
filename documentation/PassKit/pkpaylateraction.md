# PKPayLaterAction

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

Values you use to set the Apple Pay Later action.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS 1.0+

> **Deprecated**: Apple Pay Later is deprecated.

## Declaration

```swift
enum PKPayLaterAction
```

```c
enum PKPayLaterAction : NSInteger;
```

## Topics

### Widget behaviors
- [PKPayLaterAction.calculator](./pkpaylateraction/calculator.md)
  An action the provides the standard price breakdown calculator for Apple Pay Later.
- [PKPayLaterAction.learnMore](./pkpaylateraction/learnmore.md)
  An action that displays a button that a person can tap to learn more about Apple Pay Later.
### Initializers
- [init?(rawValue: Int)](./pkpaylateraction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Setting the user action
- [var action: PKPayLaterAction](./pkpaylaterview/action.md)
  The information style that the Apple Pay Later view presents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylateraction)*