# maximumNumberOfTouches

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of touches allowed to recognize this gesture

**Availability**:
- macOS 27.0+

## Declaration

```swift
var maximumNumberOfTouches: Int { get set }
```

```objc
@property NSInteger maximumNumberOfTouches;
```

## Discussion

Set this property to 0 to require exactly `minimumNumberOfTouches` touches to recognize the gesture. Defaults to `NSIntegerMax`.

## See Also

### Setting the number of touches
- [var minimumNumberOfTouches: Int](./minimumnumberoftouches.md)
  The minimum number of touches needed to recognize this gesture
- [var numberOfTouchesRequired: Int](./numberoftouchesrequired.md)
  The number of necessary touches on a Touch Bar for the gesture recognizer to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspangesturerecognizer/maximumnumberoftouches)*