# UIProposedSceneSizeNoPreference

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

Used as the value for a dimension of a size related preference when wanting to leave it unchanged.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
let UIProposedSceneSizeNoPreference: CGFloat
```

```c
extern const CGFloat UIProposedSceneSizeNoPreference;
```

## See Also

### Working with window geometry
- [var effectiveGeometry: UIWindowScene.Geometry](./uiwindowscene/effectivegeometry.md)
  The current values for the window scene’s geometry in system space.
- [func requestGeometryUpdate(UIWindowScene.GeometryPreferences, errorHandler: ((any Error) -> Void)?)](./uiwindowscene/requestgeometryupdate%28_,errorhandler%29.md)
  Requests an update to the window scene’s geometry using the specified geometry preferences object.
- [UIWindowScene.Geometry](./uiwindowscene/geometry.md)
  An object that provides geometry information about the window scene.
- [UIWindowScene.GeometryPreferences](./uiwindowscene/geometrypreferences.md)
  An abstract superclass for representing window scene geometry preferences.
- [UIWindowScene.GeometryPreferences.iOS](./uiwindowscene/geometrypreferences/ios.md)
  An object that represents the geometry preferences for a window scene in an iOS app.
- [UIWindowScene.GeometryPreferences.Mac](./uiwindowscene/geometrypreferences/mac.md)
  An object that represents the geometry preferences for a window scene in an app built with Mac Catalyst.
- [UIWindowScene.GeometryPreferences.Vision](./uiwindowscene/geometrypreferences/vision.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiproposedscenesizenopreference)*