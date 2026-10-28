# actualScaleFactor

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The actual scale factor that the system applied to the font during drawing.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var actualScaleFactor: CGFloat { get }
```

```objc
@property (readonly) CGFloat actualScaleFactor;
```

## Discussion

If you specified a custom value in the [`minimumScaleFactor`](./minimumscalefactor.md) property, when drawing is complete, this property contains the actual scale factor value that was used to draw the string.

## See Also

### Accessing the scale factors
- [var minimumScaleFactor: CGFloat](./minimumscalefactor.md)
  The scale factor that determines the smallest font size to use during drawing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstringdrawingcontext/actualscalefactor)*