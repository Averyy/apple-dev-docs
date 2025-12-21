# GenerationGuide

**Framework**: Foundation Models  
**Kind**: struct

Guides that control how values are generated.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct GenerationGuide<Value>
```

## Mentions

- [Categorizing and organizing data with content tags](categorizing-and-organizing-data-with-content-tags.md)

## Topics

### Getting the pattern
- [static func pattern<Output>(Regex<Output>) -> GenerationGuide<String>](generationguide/pattern(_:).md)
  Enforces that the string follows the pattern.
### Getting the element
- [static func element<Element>(GenerationGuide<Element>) -> GenerationGuide<[Element]>](generationguide/element(_:).md)
  Enforces a guide on the elements within the array.
### Getting the count
- [static count(_:)](generationguide/count(_:).md)
  Enforces that the array has exactly a certain number elements.
### Getting the constant
- [static func constant(String) -> GenerationGuide<String>](generationguide/constant(_:).md)
  Enforces that the string be precisely the given value.
- [static func anyOf([String]) -> GenerationGuide<String>](generationguide/anyof(_:).md)
  Enforces that the string be one of the provided values.
### Getting a range
- [static range(_:)](generationguide/range(_:).md)
  Enforces values fall within a range.
### Getting the minimum value
- [static minimum(_:)](generationguide/minimum(_:).md)
  Enforces a minimum value.
- [static func minimumCount<Element>(Int) -> GenerationGuide<[Element]>](generationguide/minimumcount(_:).md)
  Enforces a minimum number of elements in the array.
### Getting the maximum value
- [static maximum(_:)](generationguide/maximum(_:).md)
  Enforces a maximum value.
- [static func maximumCount<Element>(Int) -> GenerationGuide<[Element]>](generationguide/maximumcount(_:).md)
  Enforces a maximum number of elements in the array.

## See Also

- [macro Guide(description: String)](guide(description:).md)
  Allows for influencing the allowed values of properties of a [`Generable`](generable.md) type.
- [macro Guide(description:_:)](guide(description:_:).md)
  Allows for influencing the allowed values of properties of a [`Generable`](generable.md) type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationguide)*