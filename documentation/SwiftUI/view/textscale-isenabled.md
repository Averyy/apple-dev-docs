# textScale(_:isEnabled:)

**Framework**: SwiftUI  
**Kind**: method

Applies a text scale to text in the view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func textScale(_ scale: Text.Scale, isEnabled: Bool = true) -> some View
```

#### Return Value

A view with the specified text scale applied.

## Parameters

- `scale`: The text scale to apply.
- `isEnabled`: If true the text scale is applied; otherwise text scale   is unchanged.

## See Also

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
- [struct FixedTextVariant](fixedtextvariant.md)
  The default text variant preference that chooses the largest available variant.
- [struct SizeDependentTextVariant](sizedependenttextvariant.md)
  The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/textscale(_:isenabled:))*