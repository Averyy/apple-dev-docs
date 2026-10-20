# fill

**Framework**: SwiftUI  
**Kind**: property  
**Role**: Instance Property

A filled version of the variant.

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
var fill: SymbolVariants { get }
```

#### Discussion

Use this property to modify a shape variant like [`circle`](./circle-swift.type.property.md) so that it’s also filled:

```swift
Label("Circle Fill", systemImage: "flag")
    .symbolVariant(.circle.fill)
```

![A screenshot of a label that shows a flag in a filled circle](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/SymbolVariants-fill-2@2x.png)

## See Also

### Modifying a variant
- [var circle: SymbolVariants](./circle-swift.property.md)
  A version of the variant that’s encapsulated in a circle.
- [var square: SymbolVariants](./square-swift.property.md)
  A version of the variant that’s encapsulated in a square.
- [var rectangle: SymbolVariants](./rectangle-swift.property.md)
  A version of the variant that’s encapsulated in a rectangle.
- [var slash: SymbolVariants](./slash-swift.property.md)
  A slashed version of the variant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/symbolvariants/fill-swift.property)*