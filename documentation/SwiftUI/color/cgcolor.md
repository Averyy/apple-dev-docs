# cgColor

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A Core Graphics representation of the color, if available.

**Availability**:
- iOS 14.0+ - Deprecated in 27.2 (renamed: resolve(in:))
- iPadOS 14.0+ - Deprecated in 27.2 (renamed: resolve(in:))
- Mac Catalyst 14.0+ - Deprecated in 27.2 (renamed: resolve(in:))
- macOS 11.0+ - Deprecated in 27.2 (renamed: resolve(in:))
- tvOS 14.0+ - Deprecated in 27.2 (renamed: resolve(in:))
- visionOS 1.0+ - Deprecated in 27.2 (renamed: resolve(in:))
- watchOS 7.0+ - Deprecated in 27.2 (renamed: resolve(in:))

## Declaration

```swift
var cgColor: CGColor? { get }
```

#### Discussion

You can get a [`CGColor`](../../CoreGraphics/cgcolor.md) instance from a constant SwiftUI color. This includes colors you create from a Core Graphics color, from RGB or HSB components, or from constant UIKit and AppKit colors.

For a dynamic color, like one you load from an Asset Catalog using [`init(_:bundle:)`](./init%28_,bundle%29.md), or one you create from a dynamic UIKit or AppKit color, this property is `nil`. To evaluate all types of colors, use the `resolve(in:)` method.

## See Also

### Creating a color from another color
- [init(uiColor: UIColor)](./init%28uicolor%29.md)
  Creates a color from a UIKit color.
- [init(nsColor: NSColor)](./init%28nscolor%29.md)
  Creates a color from an AppKit color.
- [init(cgColor: CGColor)](./init%28cgcolor%29.md)
  Creates a color from a Core Graphics color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/cgcolor)*