# TupleSliderTickContent

**Framework**: SwiftUI  
**Kind**: struct

Slider content created from a Swift tuple of slider content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@frozen
struct TupleSliderTickContent<V, T> where V : BinaryFloatingPoint
```

## Topics

### Instance Properties
- [var value: T](tupleslidertickcontent/value.md)
### Type Aliases
- [TupleSliderTickContent.TicksCollection](tupleslidertickcontent/tickscollection.md)

## Relationships

### Conforms To
- [SliderTickContent](slidertickcontent.md)

## See Also

- [struct SliderTick](slidertick.md)
  A representation of a tick in a slider, with associated value and optional label.
- [struct SliderTickBuilder](slidertickbuilder.md)
  A result builder that constructs `SliderTick`s for use when creating a `Slider`.
- [struct SliderTickContentForEach](slidertickcontentforeach.md)
  A type of slider content that creates content by iterating over a collection.
- [protocol SliderTickContent](slidertickcontent.md)
  A type that provides content for a `SliderTickBuilder`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/tupleslidertickcontent)*