# maximumNumberOfTouches

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of fingers that can touch the view for gesture recognition.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var maximumNumberOfTouches: Int { get set }
```

```objc
@property (nonatomic) NSUInteger maximumNumberOfTouches;
```

## Mentions

- [Handling pan gestures](../handling-pan-gestures.md)

#### Discussion

The default value is [`NSUIntegerMax`](../../ObjectiveC/nsuintegermax.md).

## See Also

### Configuring the gesture recognizer
- [var minimumNumberOfTouches: Int](./minimumnumberoftouches.md)
  The minimum number of fingers that can touch the view for gesture recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipangesturerecognizer/maximumnumberoftouches)*