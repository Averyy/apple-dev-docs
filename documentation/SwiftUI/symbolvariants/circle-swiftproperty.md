# circle

**Framework**: SwiftUI  
**Kind**: property

A version of the variant that’s encapsulated in a circle.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var circle: SymbolVariants { get }
```

#### Discussion

Use this property to modify a variant like [`fill`](symbolvariants/fill-swift.property.md) so that it’s also contained in a circle:

```swift
Label("Fill Circle", systemImage: "bolt")
    .symbolVariant(.fill.circle)
```

![A screenshot of a label that shows a bolt in a filled circle](https://docs-assets.developer.apple.com/published/d867d29d80f41d3901708b97ef22d158/SymbolVariants-circle-2%402x.png)

## See Also

- [var square: SymbolVariants](symbolvariants/square-swift.property.md)
  A version of the variant that’s encapsulated in a square.
- [var rectangle: SymbolVariants](symbolvariants/rectangle-swift.property.md)
  A version of the variant that’s encapsulated in a rectangle.
- [var fill: SymbolVariants](symbolvariants/fill-swift.property.md)
  A filled version of the variant.
- [var slash: SymbolVariants](symbolvariants/slash-swift.property.md)
  A slashed version of the variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolvariants/circle-swift.property)*