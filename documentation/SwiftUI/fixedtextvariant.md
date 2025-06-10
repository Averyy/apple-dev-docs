# FixedTextVariant

**Framework**: SwiftUI  
**Kind**: struct

The default text variant preference that chooses the largest available variant.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct FixedTextVariant
```

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TextVariantPreference](textvariantpreference.md)

## See Also

- [func textScale(Text.Scale, isEnabled: Bool) -> some View](view/textscale(_:isenabled:).md)
  Applies a text scale to text in the view.
- [func dynamicTypeSize(_:)](view/dynamictypesize(_:).md)
  Sets the Dynamic Type size within the view to the given value.
- [var dynamicTypeSize: DynamicTypeSize](environmentvalues/dynamictypesize.md)
  The current Dynamic Type size.
- [enum DynamicTypeSize](dynamictypesize.md)
  A Dynamic Type size, which specifies how large scalable content should be.
- [struct ScaledMetric](scaledmetric.md)
  A dynamic property that scales a numeric value.
- [protocol TextVariantPreference](textvariantpreference.md)
  A protocol for controlling the size variant of text views.
- [struct SizeDependentTextVariant](sizedependenttextvariant.md)
  The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fixedtextvariant)*