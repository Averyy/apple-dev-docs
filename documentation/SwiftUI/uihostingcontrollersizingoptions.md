# UIHostingControllerSizingOptions

**Framework**: SwiftUI  
**Kind**: struct

Options for how a hosting controller tracks its content’s size.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct UIHostingControllerSizingOptions
```

## Topics

### Getting sizing options
- [static let intrinsicContentSize: UIHostingControllerSizingOptions](uihostingcontrollersizingoptions/intrinsiccontentsize.md)
  The hosting controller’s view automatically invalidate its intrinsic content size when its ideal size changes.
- [static let preferredContentSize: UIHostingControllerSizingOptions](uihostingcontrollersizingoptions/preferredcontentsize.md)
  The hosting controller tracks its content’s ideal size in its preferred content size.
### Creating a sizing option
- [init(rawValue: Int)](uihostingcontrollersizingoptions/init(rawvalue:).md)
  Creates a new option set from a raw value.
- [let rawValue: Int](uihostingcontrollersizingoptions/rawvalue.md)
  The raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Using SwiftUI with UIKit](../UIKit/using-swiftui-with-uikit.md)
  Learn how to incorporate SwiftUI views into a UIKit app.
- [Unifying your app’s animations](unifying-your-app-s-animations.md)
  Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [class UIHostingController](uihostingcontroller.md)
  A UIKit view controller that manages a SwiftUI view hierarchy.
- [struct UIHostingConfiguration](uihostingconfiguration.md)
  A content configuration suitable for hosting a hierarchy of SwiftUI views.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingcontrollersizingoptions)*