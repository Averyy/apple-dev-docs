# minimumNumberOfTouches

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum number of touches needed to recognize this gesture

**Availability**:
- macOS 27.0+

## Declaration

```swift
var minimumNumberOfTouches: Int { get set }
```

```objc
@property NSInteger minimumNumberOfTouches;
```

## Discussion

Defaults to 1.

## See Also

### Setting the number of touches
- [var maximumNumberOfTouches: Int](./maximumnumberoftouches.md)
  The maximum number of touches allowed to recognize this gesture
- [var numberOfTouchesRequired: Int](./numberoftouchesrequired.md)
  The number of necessary touches on a Touch Bar for the gesture recognizer to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspangesturerecognizer/minimumnumberoftouches)*