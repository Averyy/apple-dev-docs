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
static func range(_ range: ClosedRange<Int>) -> GenerationGuide<Int>
```

Available when `Value` is `Int`.

**Other overloads**:

```swift
static func range(_ range: ClosedRange<Decimal>) -> GenerationGuide<Decimal>
```

```swift
static func range(_ range: ClosedRange<Double>) -> GenerationGuide<Double>
```

```swift
static func range(_ range: ClosedRange<Float>) -> GenerationGuide<Float>
```

## Discussion

Use a `range` generation guide — whose bounds are inclusive — to ensure the model produces a value that falls within a range. For example, you can specify that the level of characters in your game are between 1 and 100:

```swift
@Generable
struct GameCharacter {
    @Guide(description: "A creative name appropriate for a fantasy RPG character")
    var name: String

    @Guide(description: "A level for the character", .range(1...100))
    var level: Int
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationguide/range(_:)-1es6b)*