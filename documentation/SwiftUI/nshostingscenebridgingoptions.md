# NSHostingSceneBridgingOptions

**Framework**: SwiftUI  
**Kind**: struct

Options for how hosting views and controllers manage aspects of the associated window.

**Availability**:
- macOS 14.0+

## Declaration

```swift
struct NSHostingSceneBridgingOptions
```

## Topics

### Geting bridging options
- [static let all: NSHostingSceneBridgingOptions](nshostingscenebridgingoptions/all.md)
  The hosting view’s associated window will have both its title bars and toolbars populated with values from their respective modifiers.
- [static let title: NSHostingSceneBridgingOptions](nshostingscenebridgingoptions/title.md)
  The hosting view’s associated window will have its title and subtitle populated with the values provided to the `navigationTitle(_:)` and `navigationSubtitle(_:)` modifiers, respectively.
- [static let toolbars: NSHostingSceneBridgingOptions](nshostingscenebridgingoptions/toolbars.md)
  The hosting view’s associated window will have its toolbar populated with any items provided to the `toolbar(content:)` modifier.
### Creating a bridging options
- [init(rawValue: Int)](nshostingscenebridgingoptions/init(rawvalue:).md)
  Creates a new set from a raw value.
- [let rawValue: Int](nshostingscenebridgingoptions/rawvalue.md)
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

- [Unifying your app’s animations](unifying-your-app-s-animations.md)
  Create a consistent UI animation experience across SwiftUI, UIKit, and AppKit.
- [class NSHostingController](nshostingcontroller.md)
  An AppKit view controller that hosts SwiftUI view hierarchy.
- [class NSHostingView](nshostingview.md)
  An AppKit view that hosts a SwiftUI view hierarchy.
- [class NSHostingMenu](nshostingmenu.md)
  An AppKit menu with menu items that are defined by a SwiftUI View.
- [struct NSHostingSizingOptions](nshostingsizingoptions.md)
  Options for how hosting views and controllers reflect their content’s size into Auto Layout constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nshostingscenebridgingoptions)*