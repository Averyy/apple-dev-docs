# bounds

**Framework**: UIKit  
**Kind**: property

The bounds of the graphics context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var bounds: CGRect { get }
```

#### Discussion

This value represents the bounds of every Core Graphics context that the associated graphics renderer creates.

If the graphics renderer itself creates a format object, the bounds are set to those provided to the renderer as part of the initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigraphicsrendererformat/bounds)*