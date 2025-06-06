# magnification

**Framework**: AppKit  
**Kind**: property

The amount of magnification to apply.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var magnification: CGFloat { get set }
```

#### Discussion

This property contains the current magnification in effect for the gesture. Add the value of this property to `1.0` to get the scale factor to apply to your content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsmagnificationgesturerecognizer/magnification)*