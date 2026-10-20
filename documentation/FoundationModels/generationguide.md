# GenerationGuide

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

Guides that control how values are generated.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
struct GenerationGuide<Value>
```

## Mentions

- [Categorizing and organizing data with content tags](./categorizing-and-organizing-data-with-content-tags.md)

## Topics

### Getting the pattern
- [static func pattern<Output>(Regex<Output>) -> GenerationGuide<String>](./generationguide/pattern%28_%29.md)
  Enforces that the string follows the pattern.
### Getting the element
- [static func element<Element>(GenerationGuide<Element>) -> GenerationGuide<[Element]>](./generationguide/element%28_%29.md)
  Enforces a guide on the elements within the array.
### Getting the count
- [static count(_:)](./generationguide/count%28_%29.md)
  Enforces that the array has exactly a certain number of elements.
### Getting the constant
- [static func constant(String) -> GenerationGuide<String>](./generationguide/constant%28_%29.md)
  Enforces that the string be precisely the given value.
- [static func anyOf([String]) -> GenerationGuide<String>](./generationguide/anyof%28_%29.md)
  Enforces that the string be one of the provided values.
### Getting a range
- [static range(_:)](./generationguide/range%28_%29.md)
  Enforces values that fall within a range.
### Getting the minimum value
- [static minimum(_:)](./generationguide/minimum%28_%29.md)
  Enforces a minimum value.
- [static func minimumCount<Element>(Int) -> GenerationGuide<[Element]>](./generationguide/minimumcount%28_%29.md)
  Enforces a minimum number of elements in the array.
### Getting the maximum value
- [static maximum(_:)](./generationguide/maximum%28_%29.md)
  Enforces a maximum value.
- [static func maximumCount<Element>(Int) -> GenerationGuide<[Element]>](./generationguide/maximumcount%28_%29.md)
  Enforces a maximum number of elements in the array.

## See Also

### Creating a guide
- [macro Guide(description: String)](./guide%28description%29.md)
- [macro Guide(description:_:)](./guide%28description,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationguide)*