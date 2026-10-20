# ScaledMetric

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A dynamic property that scales a numeric value.

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
@propertyWrapper
struct ScaledMetric<Value> where Value : BinaryFloatingPoint
```

## Mentions

- [Applying custom fonts to text](./applying-custom-fonts-to-text.md)

## Topics

### Creating the metric
- [init(wrappedValue: Value)](./scaledmetric/init%28wrappedvalue%29.md)
  Creates the scaled metric with an unscaled value using the default scaling.
- [init(wrappedValue: Value, relativeTo: Font.TextStyle)](./scaledmetric/init%28wrappedvalue,relativeto%29.md)
  Creates the scaled metric with an unscaled value and a text style to scale relative to.
### Getting the metric
- [var wrappedValue: Value](./scaledmetric/wrappedvalue.md)
  The value scaled based on the current environment.

## Relationships

### Conforms To
- [DynamicProperty](./dynamicproperty.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Adjusting text size
- [func textScale(Text.Scale, isEnabled: Bool) -> some View](./view/textscale%28_,isenabled%29.md)
  Applies a text scale to text in the view.
- [func dynamicTypeSize(_:)](./view/dynamictypesize%28_%29.md)
  Sets the Dynamic Type size within the view to the given value.
- [var dynamicTypeSize: DynamicTypeSize](./environmentvalues/dynamictypesize.md)
  The current Dynamic Type size.
- [enum DynamicTypeSize](./dynamictypesize.md)
  A Dynamic Type size, which specifies how large scalable content should be.
- [protocol TextVariantPreference](./textvariantpreference.md)
  A protocol for controlling the size variant of text views.
- [struct FixedTextVariant](./fixedtextvariant.md)
  The default text variant preference that chooses the largest available variant.
- [struct SizeDependentTextVariant](./sizedependenttextvariant.md)
  The size dependent variant preference allows the text to take the available space into account when choosing the variant to display.
- [enum ContentSizeCategory](./contentsizecategory.md)
  The sizes that you can specify for content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/scaledmetric)*