# effectiveCornerRadii

**Framework**: AppKit  
**Kind**: property

The effective radius of each corner in the view, calculated based on the corner configuration (`cornerConfiguration`). This value is `nil` when the corner configuration is `nil`.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
@NSCopying
var effectiveCornerRadii: NSViewCornerRadii? { get }
```

## See Also

- [var cornerConfiguration: NSViewCornerConfiguration?](nsview/cornerconfiguration.md)
  Defines the corner styles (e.g., square, capsule, concentric, etc) for the view’s corners.
- [func invalidateCornerConfiguration()](nsview/invalidatecornerconfiguration.md)
  Invalidates the corner configuration, causing both the configuration and its dependencies to be recomputed.
- [func viewDidChangeEffectiveCornerRadii()](nsview/viewdidchangeeffectivecornerradii.md)
  Informs the view that its effective corner radii changed. This method should be overridden to apply the corner radii to the view as required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/effectivecornerradii)*