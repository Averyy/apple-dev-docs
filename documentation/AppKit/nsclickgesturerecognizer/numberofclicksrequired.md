# numberOfClicksRequired

**Framework**: AppKit  
**Kind**: property

The number of clicks required to match.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var numberOfClicksRequired: Int { get set }
```

#### Discussion

The value in this property should always be a positive integer. Negative integers or `0` cause this object to never recognize its gesture. The default value of this property is `1`.

## See Also

- [var buttonMask: Int](nsclickgesturerecognizer/buttonmask.md)
  A bit mask of the button (or buttons) required to recognize this click.
- [var numberOfTouchesRequired: Int](nsclickgesturerecognizer/numberoftouchesrequired.md)
  The number of touches required in an [`NSTouchBar`](nstouchbar.md) object for the gesture recognizer to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclickgesturerecognizer/numberofclicksrequired)*