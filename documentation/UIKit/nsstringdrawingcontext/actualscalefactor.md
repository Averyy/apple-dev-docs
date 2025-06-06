# actualScaleFactor

**Framework**: UIKit  
**Kind**: property

The actual scale factor that the system applied to the font during drawing.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var actualScaleFactor: CGFloat { get }
```

#### Discussion

If you specified a custom value in the [`minimumScaleFactor`](nsstringdrawingcontext/minimumscalefactor.md) property, when drawing is complete, this property contains the actual scale factor value that was used to draw the string.

## See Also

- [var minimumScaleFactor: CGFloat](nsstringdrawingcontext/minimumscalefactor.md)
  The scale factor that determines the smallest font size to use during drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsstringdrawingcontext/actualscalefactor)*