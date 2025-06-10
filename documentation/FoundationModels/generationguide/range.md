# range(_:)

**Framework**: Foundation Models  
**Kind**: method

Enforces values fall within a range.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func range(_ range: ClosedRange<Decimal>) -> GenerationGuide<Decimal>
```

#### Discussion

Use a `range` generation guide — whose bounds are inclusive — to ensure the model produces a value that falls within a range. For example, you can specify that the level of characters in your game are between 1 and 100:

```swift
@Generable
struct struct GameCharacter {
    @Guide(description: "A creative name appropriate for a fantasy RPG character"
    var name: String

    @Guide(description: "A level for the character", .range(1...100))
    var level: Int
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationguide/range(_:))*