# SliderTick

**Framework**: SwiftUI  
**Kind**: struct

A representation of a tick in a slider, with associated value and optional label.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct SliderTick<V> where V : BinaryFloatingPoint
```

#### Overview

The following example shows a slider bound to the value `percentage`. As the slider updates the `currentValueLabel`. The slider also renders marks at a `0.25` step interval.

```swift
@State private var percentage = 0.5

Slider(value: $percentage) {
    Text("Percentage")
} currentValueLabel: {
    Text("\(percentage)%")
} ticks: {
    SliderTickContentForEach(
        stride(from: 0.0, through: 1.0, by: 0.25).map { $0 },
        id: \.self
    ) { value in
        SliderTick(value) {
            label(for: value)
        }
    }
}
```

## Topics

### Structures
- [SliderTick.ID](slidertick/id-swift.struct.md)
  The identity of a tick.
### Initializers
- [init(_:)](slidertick/init(_:).md)
  Create a labeled slider tick at a specific value.
- [init(_:_:)](slidertick/init(_:_:).md)
  Create a slider tick with a label from a localized string key.
- [init(V, label: () -> some View)](slidertick/init(_:label:).md)
  Create a labeled slider tick at a specific value.
### Instance Properties
- [var id: SliderTick<V>.ID](slidertick/id-swift.property.md)
  The identity of a tick, which is derived from its value.

## Relationships

### Conforms To
- [Comparable](../Swift/Comparable.md)
- [Equatable](../Swift/Equatable.md)
- [Identifiable](../Swift/Identifiable.md)
- [SliderTickContent](slidertickcontent.md)

## See Also

- [struct SliderTickBuilder](slidertickbuilder.md)
  A result builder that constructs `SliderTick`s for use when creating a `Slider`.
- [struct SliderTickContentForEach](slidertickcontentforeach.md)
  A type of slider content that creates content by iterating over a collection.
- [struct TupleSliderTickContent](tupleslidertickcontent.md)
  Slider content created from a Swift tuple of slider content.
- [protocol SliderTickContent](slidertickcontent.md)
  A type that provides content for a `SliderTickBuilder`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slidertick)*