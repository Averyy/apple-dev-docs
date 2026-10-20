# cornerConfiguration

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Defines the corner styles (e.g., square, capsule, concentric, etc) for the view’s corners.

**Availability**:
- macOS 27.0+

## Declaration

```swift
@NSCopying
var cornerConfiguration: NSViewCornerConfiguration? { get }
```

```objc
@property (copy, readonly, nullable) NSViewCornerConfiguration * cornerConfiguration;
```

## See Also

### Configuring corners
- [var effectiveCornerRadii: NSViewCornerRadii?](./effectivecornerradii.md)
  The effective radius of each corner in the view, calculated based on the corner configuration (`cornerConfiguration`). This value is `nil` when the corner configuration is `nil`.
- [func invalidateCornerConfiguration()](./invalidatecornerconfiguration%28%29.md)
  Invalidates the corner configuration, causing both the configuration and its dependencies to be recomputed.
- [func viewDidChangeEffectiveCornerRadii()](./viewdidchangeeffectivecornerradii%28%29.md)
  Informs the view that its effective corner radii changed. This method should be overridden to apply the corner radii to the view as required.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/cornerconfiguration)*