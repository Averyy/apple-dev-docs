# UIHostingControllerSizingOptions

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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
- [static let intrinsicContentSize: UIHostingControllerSizingOptions](./uihostingcontrollersizingoptions/intrinsiccontentsize.md)
  The hosting controller’s view automatically invalidate its intrinsic content size when its ideal size changes.
- [static let preferredContentSize: UIHostingControllerSizingOptions](./uihostingcontrollersizingoptions/preferredcontentsize.md)
  The hosting controller tracks its content’s ideal size in its preferred content size.
### Creating a sizing option
- [init(rawValue: Int)](./uihostingcontrollersizingoptions/init%28rawvalue%29.md)
  Creates a new option set from a raw value.
- [let rawValue: Int](./uihostingcontrollersizingoptions/rawvalue.md)
  The raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Displaying SwiftUI views in UIKit
- [Using SwiftUI with UIKit](../UIKit/using-swiftui-with-uikit.md)
  Learn how to incorporate SwiftUI views into a UIKit app.
- [Unifying your app’s animations](./unifying-your-app-s-animations.md)
  Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [class UIHostingController](./uihostingcontroller.md)
  A UIKit view controller that manages a SwiftUI view hierarchy.
- [struct UIHostingConfiguration](./uihostingconfiguration.md)
  A content configuration suitable for hosting a hierarchy of SwiftUI views.
- [protocol UIHostingSceneDelegate](./uihostingscenedelegate.md)
  Extends `UIKit/UISceneDelegate` to bridge SwiftUI scenes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uihostingcontrollersizingoptions)*