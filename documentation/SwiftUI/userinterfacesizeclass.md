# UserInterfaceSizeClass

**Framework**: SwiftUI  
**Kind**: enum

A set of values that indicate the visual size available to the view.

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
enum UserInterfaceSizeClass
```

#### Overview

You receive a size class value when you read either the [`horizontalSizeClass`](environmentvalues/horizontalsizeclass.md) or [`verticalSizeClass`](environmentvalues/verticalsizeclass.md) environment value. The value tells you about the amount of space available to your views in a given direction. You can read the size class like any other of the [`EnvironmentValues`](environmentvalues.md), by creating a property with the [`Environment`](environment.md) property wrapper:

```swift
@Environment(\.horizontalSizeClass) private var horizontalSizeClass
@Environment(\.verticalSizeClass) private var verticalSizeClass
```

SwiftUI sets the size class based on several factors, including:

- The current device type.
- The orientation of the device.
- The appearance of Slide Over and Split View on iPad.

Several built-in views change their behavior based on the size class. For example, a [`NavigationView`](navigationview.md) presents a multicolumn view when the horizontal size class is [`UserInterfaceSizeClass.regular`](userinterfacesizeclass/regular.md), but a single column otherwise. You can also adjust the appearance of custom views by reading the size class and conditioning your views. If you do, be prepared to handle size class changes while your app runs, because factors like device orientation can change at runtime.

## Topics

### Getting size classes
- [UserInterfaceSizeClass.compact](userinterfacesizeclass/compact.md)
  The compact size class.
- [UserInterfaceSizeClass.regular](userinterfacesizeclass/regular.md)
  The regular size class.
### Creating a size class
- [init?(UIUserInterfaceSizeClass)](userinterfacesizeclass/init(_:).md)
  Creates a SwiftUI size class from the specified UIKit size class.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isLuminanceReduced: Bool](environmentvalues/isluminancereduced.md)
  A Boolean value that indicates whether the display or environment currently requires reduced luminance.
- [var displayScale: CGFloat](environmentvalues/displayscale.md)
  The display scale of this environment.
- [var pixelLength: CGFloat](environmentvalues/pixellength.md)
  The size of a pixel on the screen.
- [var horizontalSizeClass: UserInterfaceSizeClass?](environmentvalues/horizontalsizeclass.md)
  The horizontal size class of this environment.
- [var verticalSizeClass: UserInterfaceSizeClass?](environmentvalues/verticalsizeclass.md)
  The vertical size class of this environment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/userinterfacesizeclass)*