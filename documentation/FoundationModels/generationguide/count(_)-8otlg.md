# count(_:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

Enforces that the number of elements in the array falls within a closed range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
static func count<Element>(_ range: ClosedRange<Int>) -> GenerationGuide<[Element]> where Value == [Element]
```

**Other overloads**:

```swift
static func count<Element>(_ count: Int) -> GenerationGuide<[Element]> where Value == [Element]
```

## Discussion

Bounds are inclusive.

A `count` generation guide may be used when you want to ensure the model produces a number of array elements that falls within a given range, such as the number of items in a game’s shop.

```swift
@Generable
struct Shop {
    @Guide(description: "A creative name for a shop in a fantasy RPG")
    var name: String

    @Guide(description: "A list of items for sale", .count(2...10))
    var inventory: [ShopItem]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationguide/count(_:)-8otlg)*