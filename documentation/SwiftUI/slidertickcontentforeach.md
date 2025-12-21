# SliderTickContentForEach

**Framework**: SwiftUI  
**Kind**: struct

A type of slider content that creates content by iterating over a collection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct SliderTickContentForEach<Data, ID, Content> where Data : RandomAccessCollection, ID : Hashable, Content : SliderTickContent
```

## Topics

### Initializers
- [init(_:content:)](slidertickcontentforeach/init(_:content:).md)
  Creates an instance that uniquely identifies and creates slider ticks across updates based on the identity of the underlying data.
- [init<V>(Data, id: KeyPath<Data.Element, ID>, content: (Data.Element) -> Content)](slidertickcontentforeach/init(_:id:content:).md)
  Creates an instance that uniquely identifies and creates slider ticks across updates based on the provided key path to the underlying data’s identifier.

## Relationships

### Conforms To
- [SliderTickContent](slidertickcontent.md)

## See Also

- [struct SliderTick](slidertick.md)
  A representation of a tick in a slider, with associated value and optional label.
- [struct SliderTickBuilder](slidertickbuilder.md)
  A result builder that constructs `SliderTick`s for use when creating a `Slider`.
- [struct TupleSliderTickContent](tupleslidertickcontent.md)
  Slider content created from a Swift tuple of slider content.
- [protocol SliderTickContent](slidertickcontent.md)
  A type that provides content for a `SliderTickBuilder`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slidertickcontentforeach)*