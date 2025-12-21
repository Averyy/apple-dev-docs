# maximumCount(_:)

**Framework**: Foundation Models  
**Kind**: method

Enforces a maximum number of elements in the array.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func maximumCount<Element>(_ count: Int) -> GenerationGuide<[Element]> where Value == [Element]
```

## Mentions

- [Categorizing and organizing data with content tags](categorizing-and-organizing-data-with-content-tags.md)

#### Discussion

The bounds are inclusive.

A `maximumCount` generation guide may be used when you want to ensure the model produces a number of array elements less than or equal to to some maximum value, such as the number of items in a game’s shop.

```swift
@Generable
struct struct Shop {
    @Guide(description: "A creative name for a shop in a fantasy RPG"
    var name: String

    @Guide(description: "A list of items for sale", .maximumCount(10))
    var inventory: [ShopItem]
}
```

## See Also

- [static maximum(_:)](generationguide/maximum(_:).md)
  Enforces a maximum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationguide/maximumcount(_:))*