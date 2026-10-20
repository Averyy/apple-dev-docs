# minimumCount(_:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

Enforces a minimum number of elements in the array.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
static func minimumCount<Element>(_ count: Int) -> GenerationGuide<[Element]> where Value == [Element]
```

#### Discussion

The bounds are inclusive.

A `minimumCount` generation guide may be used when you want to ensure the model produces a number of array elements greater than or equal to some minimum value, such as the number of items in a game’s shop.

```swift
@Generable
struct Shop {
    @Guide(description: "A creative name for a shop in a fantasy RPG")
    var name: String

    @Guide(description: "A list of items for sale", .minimumCount(3))
    var inventory: [ShopItem]
}
```

## See Also

### Getting the minimum value
- [static minimum(_:)](./minimum%28_%29.md)
  Enforces a minimum value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationguide/minimumcount(_:))*