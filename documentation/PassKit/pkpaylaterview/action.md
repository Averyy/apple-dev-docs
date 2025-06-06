# action

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The information style that the Apple Pay Later view presents.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var action: PKPayLaterAction { get set }
```

#### Discussion

This property determines the kind of information modal the Apple Pay Later visual merchandising widget displays. The default is [`PKPayLaterAction.learnMore`](pkpaylateraction/learnmore.md).

## See Also

- [enum PKPayLaterAction](pkpaylateraction.md)
  Values you use to set the Apple Pay Later action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylaterview/action)*