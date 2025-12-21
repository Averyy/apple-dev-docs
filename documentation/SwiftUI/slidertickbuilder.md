# SliderTickBuilder

**Framework**: SwiftUI  
**Kind**: struct

A result builder that constructs `SliderTick`s for use when creating a `Slider`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@resultBuilder
struct SliderTickBuilder<V> where V : BinaryFloatingPoint
```

## Topics

### Type Methods
- [static func buildBlock() -> some SliderTickContent<V>
](slidertickbuilder/buildblock.md)
  Creates a single slider content result.
- [static func buildBlock(some SliderTickContent<V>) -> some SliderTickContent<V>
](slidertickbuilder/buildblock(_:).md)
  Creates a single slider content result.
- [static func buildBlock<C0, C1>(C0, C1) -> some SliderTickContent<V>
](slidertickbuilder/buildblock(_:_:).md)
- [static func buildBlock<C0, C1, C2>(C0, C1, C2) -> some SliderTickContent<V>
](slidertickbuilder/buildblock(_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3>(C0, C1, C2, C3) -> some SliderTickContent<V>
](slidertickbuilder/buildblock(_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4>(C0, C1, C2, C3, C4) -> some SliderTickContent<V>
](slidertickbuilder/buildblock(_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5>(C0, C1, C2, C3, C4, C5) -> some SliderTickContent<V>
](slidertickbuilder/buildblock(_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6>(C0, C1, C2, C3, C4, C5, C6) -> some SliderTickContent<V>
](slidertickbuilder/buildblock(_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7>(C0, C1, C2, C3, C4, C5, C6, C7) -> some SliderTickContent<V>
](slidertickbuilder/buildblock(_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8>(C0, C1, C2, C3, C4, C5, C6, C7, C8) -> some SliderTickContent<V>
](slidertickbuilder/buildblock(_:_:_:_:_:_:_:_:_:).md)
- [static func buildBlock<C0, C1, C2, C3, C4, C5, C6, C7, C8, C9>(C0, C1, C2, C3, C4, C5, C6, C7, C8, C9) -> some SliderTickContent<V>
](slidertickbuilder/buildblock(_:_:_:_:_:_:_:_:_:_:).md)
- [static func buildEither<T, F>(first: T) -> _ConditionalContent<T, F>](slidertickbuilder/buildeither(first:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [static func buildEither<T, F>(second: F) -> _ConditionalContent<T, F>](slidertickbuilder/buildeither(second:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [static func buildExpression(some SliderTickContent<V>) -> some SliderTickContent<V>
](slidertickbuilder/buildexpression(_:).md)
  Creates a single slider content expression.
- [static func buildIf(some SliderTickContent<V>) -> some SliderTickContent<V>
](slidertickbuilder/buildif(_:).md)
  Produces an optional slider content for conditional statements in multi-statement closures that’s only visible when the condition evaluates to true.

## See Also

- [struct SliderTick](slidertick.md)
  A representation of a tick in a slider, with associated value and optional label.
- [struct SliderTickContentForEach](slidertickcontentforeach.md)
  A type of slider content that creates content by iterating over a collection.
- [struct TupleSliderTickContent](tupleslidertickcontent.md)
  Slider content created from a Swift tuple of slider content.
- [protocol SliderTickContent](slidertickcontent.md)
  A type that provides content for a `SliderTickBuilder`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/slidertickbuilder)*