# verticalSizeClass

**Framework**: SwiftUI  
**Kind**: property

The vertical size class of this environment.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@backDeployed(before: macOS 14.0, tvOS 17.0, watchOS 10.0)
var verticalSizeClass: UserInterfaceSizeClass? { get set }
```

#### Discussion

You receive a [`UserInterfaceSizeClass`](userinterfacesizeclass.md) value when you read this environment value. The value tells you about the amount of vertical space available to the view that reads it. You can read this size class like any other of the [`EnvironmentValues`](environmentvalues.md), by creating a property with the [`Environment`](environment.md) property wrapper:

```swift
@Environment(\.verticalSizeClass) private var verticalSizeClass
```

SwiftUI sets this size class based on several factors, including:

- The current device type.
- The orientation of the device.

You can adjust the appearance of custom views by reading this size class and conditioning your views. If you do, be prepared to handle size class changes while your app runs, because factors like device orientation can change at runtime.

In watchOS, the vertical size class is always [`UserInterfaceSizeClass.compact`](userinterfacesizeclass/compact.md). In macOS, and tvOS, it’s always [`UserInterfaceSizeClass.regular`](userinterfacesizeclass/regular.md).

Writing to the vertical size class in the environment before macOS 14.0, tvOS 17.0, and watchOS 10.0 is not supported.

## See Also

- [var isLuminanceReduced: Bool](environmentvalues/isluminancereduced.md)
  A Boolean value that indicates whether the display or environment currently requires reduced luminance.
- [var displayScale: CGFloat](environmentvalues/displayscale.md)
  The display scale of this environment.
- [var pixelLength: CGFloat](environmentvalues/pixellength.md)
  The size of a pixel on the screen.
- [var horizontalSizeClass: UserInterfaceSizeClass?](environmentvalues/horizontalsizeclass.md)
  The horizontal size class of this environment.
- [enum UserInterfaceSizeClass](userinterfacesizeclass.md)
  A set of values that indicate the visual size available to the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/environmentvalues/verticalsizeclass)*