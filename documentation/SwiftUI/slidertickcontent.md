# SliderTickContent

**Framework**: SwiftUI  
**Kind**: protocol

A type that provides content for a `SliderTickBuilder`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
protocol SliderTickContent<Value>
```

## Topics

### Associated Types
- [associatedtype Body : RandomAccessCollection](slidertickcontent/body-swift.associatedtype.md)
- [associatedtype Value : BinaryFloatingPoint](slidertickcontent/value.md)
### Instance Properties
- [var body: Self.Body](slidertickcontent/body-swift.property.md)
  The value of this type’s content.

## Relationships

### Conforming Types
- [SliderTick](slidertick.md)
- [SliderTickContentForEach](slidertickcontentforeach.md)
- [TupleSliderTickContent](tupleslidertickcontent.md)

## See Also

- [struct SliderTick](slidertick.md)
  A representation of a tick in a slider, with associated value and optional label.
- [struct SliderTickBuilder](slidertickbuilder.md)
  A result builder that constructs `SliderTick`s for use when creating a `Slider`.
- [struct SliderTickContentForEach](slidertickcontentforeach.md)
  A type of slider content that creates content by iterating over a collection.
- [struct TupleSliderTickContent](tupleslidertickcontent.md)
  Slider content created from a Swift tuple of slider content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slidertickcontent)*