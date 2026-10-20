# minimumNumberOfTouches

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The minimum number of fingers that can touch the view for gesture recognition.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var minimumNumberOfTouches: Int { get set }
```

```objc
@property (nonatomic) NSUInteger minimumNumberOfTouches;
```

## Mentions

- [Handling pan gestures](../handling-pan-gestures.md)

#### Discussion

The default value is `1`.

## See Also

### Configuring the gesture recognizer
- [var maximumNumberOfTouches: Int](./maximumnumberoftouches.md)
  The maximum number of fingers that can touch the view for gesture recognition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipangesturerecognizer/minimumnumberoftouches)*