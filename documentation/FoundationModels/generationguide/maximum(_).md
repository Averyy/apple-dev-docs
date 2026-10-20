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
static func maximum(_ value: Decimal) -> GenerationGuide<Decimal>
```

Available when `Value` is `Decimal`.

**Other overloads**:

```swift
static func maximum(_ value: Double) -> GenerationGuide<Double>
```

```swift
static func maximum(_ value: Float) -> GenerationGuide<Float>
```

```swift
static func maximum(_ value: Int) -> GenerationGuide<Int>
```

#### Discussion

Use a `maximum` generation guide — whose bounds are inclusive — to ensure the model produces a value less than or equal to some maximum value. For example, you can specify that the highest level a character in your game can achieve is 99.9:

```swift
@Generable
struct GameCharacter {
    @Guide(description: "A creative name appropriate for a fantasy RPG character")
    var name: String

    @Guide(description: "A level for the character", .maximum(99.9))
    var level: Decimal
}
```

## See Also

### Getting the maximum value
- [static func maximumCount<Element>(Int) -> GenerationGuide<[Element]>](./maximumcount%28_%29.md)
  Enforces a maximum number of elements in the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationguide/maximum(_:))*