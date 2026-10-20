# range(_:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

Enforces values that fall within a range.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
static func range(_ range: ClosedRange<Decimal>) -> GenerationGuide<Decimal>
```

Available when `Value` is `Decimal`.

**Other overloads**:

```swift
static func range(_ range: ClosedRange<Double>) -> GenerationGuide<Double>
```

```swift
static func range(_ range: ClosedRange<Float>) -> GenerationGuide<Float>
```

```swift
static func range(_ range: ClosedRange<Int>) -> GenerationGuide<Int>
```

#### Discussion

Bounds are inclusive.

A `range` generation guide may be used when you want to ensure the model produces a value that falls in some range, such as the cost for an item in a game.

```swift
@Generable
struct ShopItem {
    @Guide(description: "A creative name for an item sold in a fantasy RPG")
    var name: String

    @Guide(description: "A cost for the item", .range(0.25...1000))
    var cost: Decimal
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationguide/range(_:))*