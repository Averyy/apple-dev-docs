# physicalMetrics

**Framework**: SwiftUI  
**Kind**: property

The physical metrics associated with a scene.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var physicalMetrics: PhysicalMetricsConverter { get set }
```

#### Discussion

Reading this value returns a `PhysicalMetricsConverter` corresponding to the window scene associated with the environment’s reader. The converter can convert point sizes into physical measurements of length, and vice versa.

Reading this value is only supported in the body of a [`View`](view.md) or of a type that inherits a [`View`](view.md)’s environment.

## See Also

- [var allowedDynamicRange: Image.DynamicRange?](environmentvalues/alloweddynamicrange.md)
  The allowed dynamic range for the view, or nil.
- [var backgroundMaterial: Material?](environmentvalues/backgroundmaterial.md)
  The material underneath the current view.
- [var backgroundProminence: BackgroundProminence](environmentvalues/backgroundprominence.md)
  The prominence of the background underneath views associated with this environment.
- [var backgroundStyle: AnyShapeStyle?](environmentvalues/backgroundstyle.md)
  An optional style that overrides the default system background style when set.
- [var badgeProminence: BadgeProminence](environmentvalues/badgeprominence.md)
  The prominence to apply to badges associated with this environment.
- [var contentTransition: ContentTransition](environmentvalues/contenttransition.md)
  The current method of animating the contents of views.
- [var contentTransitionAddsDrawingGroup: Bool](environmentvalues/contenttransitionaddsdrawinggroup.md)
  A Boolean value that controls whether views that render content transitions use GPU-accelerated rendering.
- [var defaultMinListHeaderHeight: CGFloat?](environmentvalues/defaultminlistheaderheight.md)
  The default minimum height of a header in a list.
- [var defaultMinListRowHeight: CGFloat](environmentvalues/defaultminlistrowheight.md)
  The default minimum height of a row in a `List`. The default minimum height of a row in a list.
- [var headerProminence: Prominence](environmentvalues/headerprominence.md)
  The prominence to apply to section headers within a view.
- [var realityKitScene: Scene?](environmentvalues/realitykitscene.md)
- [var realityViewCameraControls: CameraControls](environmentvalues/realityviewcameracontrols.md)
  The camera controls for the reality view.
- [var redactionReasons: RedactionReasons](environmentvalues/redactionreasons.md)
  The current redaction reasons applied to the view hierarchy.
- [var springLoadingBehavior: SpringLoadingBehavior](environmentvalues/springloadingbehavior.md)
  The behavior of spring loaded interactions for the views associated with this environment.
- [var symbolRenderingMode: SymbolRenderingMode?](environmentvalues/symbolrenderingmode.md)
  The current symbol rendering mode, or `nil` denoting that the mode is picked automatically using the current image and foreground style as parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/physicalmetrics)*