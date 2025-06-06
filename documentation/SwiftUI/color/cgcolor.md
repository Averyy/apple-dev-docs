# cgColor

**Framework**: SwiftUI  
**Kind**: property

A Core Graphics representation of the color, if available.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var cgColor: CGColor? { get }
```

#### Discussion

You can get a [`CGColor`](https://developer.apple.com/documentation/CoreGraphics/CGColor) instance from a constant SwiftUI color. This includes colors you create from a Core Graphics color, from RGB or HSB components, or from constant UIKit and AppKit colors.

For a dynamic color, like one you load from an Asset Catalog using [`init(_:bundle:)`](color/init(_:bundle:).md), or one you create from a dynamic UIKit or AppKit color, this property is `nil`. To evaluate all types of colors, use the `resolve(in:)` method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/color/cgcolor)*