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
static func maximum(_ value: Int) -> GenerationGuide<Int>
```

Available when `Value` is `Int`.

**Other overloads**:

```swift
static func maximum(_ value: Decimal) -> GenerationGuide<Decimal>
```

```swift
static func maximum(_ value: Double) -> GenerationGuide<Double>
```

```swift
static func maximum(_ value: Float) -> GenerationGuide<Float>
```

## Discussion

Use a `maximum` generation guide — whose bounds are inclusive — to ensure the model produces a value less than or equal to some maximum value. For example, you can specify that the highest level a character in your game can achieve is 100:

```swift
@Generable
struct GameCharacter {
    @Guide(description: "A creative name appropriate for a fantasy RPG character")
    var name: String

    @Guide(description: "A level for the character", .maximum(100))
    var level: Int
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationguide/maximum(_:)-39jvl)*