# physicalMetrics

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

The physical metrics associated with a scene.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var physicalMetrics: PhysicalMetricsConverter { get set }
```

## Discussion

Reading this value returns a `PhysicalMetricsConverter` corresponding to the window scene associated with the environment’s reader. The converter can convert point sizes into physical measurements of length, and vice versa.

Reading this value is only supported in the body of a [`View`](../view.md) or of a type that inherits a [`View`](../view.md)’s environment.

## See Also

### View attributes
- [var allowedDynamicRange: Image.DynamicRange?](./alloweddynamicrange.md)
  The allowed dynamic range for the view, or nil.
- [var backgroundMaterial: Material?](./backgroundmaterial.md)
  The material underneath the current view.
- [var backgroundProminence: BackgroundProminence](./backgroundprominence.md)
  The prominence of the background underneath views associated with this environment.
- [var backgroundStyle: AnyShapeStyle?](./backgroundstyle.md)
  An optional style that overrides the default system background style when set.
- [var badgeProminence: BadgeProminence](./badgeprominence.md)
  The prominence to apply to badges associated with this environment.
- [var contentTransition: ContentTransition](./contenttransition.md)
  The current method of animating the contents of views.
- [var contentTransitionAddsDrawingGroup: Bool](./contenttransitionaddsdrawinggroup.md)
  A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [var defaultMinListHeaderHeight: CGFloat?](./defaultminlistheaderheight.md)
  The default minimum height of a header in a list.
- [var defaultMinListRowHeight: CGFloat](./defaultminlistrowheight.md)
  The default minimum height of rows in a list.
- [var headerProminence: Prominence](./headerprominence.md)
  The prominence to apply to section headers within a view.
- [var realityKitScene: Scene?](./realitykitscene.md)
- [var realityViewCameraControls: CameraControls](./realityviewcameracontrols.md)
  The camera controls for the reality view.
- [var redactionReasons: RedactionReasons](./redactionreasons.md)
  The current redaction reasons applied to the view hierarchy.
- [var springLoadingBehavior: SpringLoadingBehavior](./springloadingbehavior.md)
  The behavior of spring loaded interactions for the views associated with this environment.
- [var symbolRenderingMode: SymbolRenderingMode?](./symbolrenderingmode.md)
  The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/physicalmetrics)*