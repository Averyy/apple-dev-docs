# maximum(_:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Type Method

Enforces a maximum value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+
- watchOS 27.0+

## Declaration

```swift
static func maximum(_ value: Double) -> GenerationGuide<Double>
```

Available when `Value` is `Double`.

**Other overloads**:

```swift
static func maximum(_ value: Decimal) -> GenerationGuide<Decimal>
```

```swift
static func maximum(_ value: Float) -> GenerationGuide<Float>
```

```swift
static func maximum(_ value: Int) -> GenerationGuide<Int>
```

## Discussion

Use a `maximum` generation guide — whose bounds are inclusive — to ensure the model produces a value less than or equal to some maximum value. For example, you can specify that the highest level a character in your game can achieve is 5000.0:

```swift
@Generable
struct GameCharacter {
    @Guide(description: "A creative name appropriate for a fantasy RPG character")
    var name: String

    @Guide(description: "A level for the character", .maximum(5000.0))
    var level: Double
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationguide/maximum(_:)-381t8)*