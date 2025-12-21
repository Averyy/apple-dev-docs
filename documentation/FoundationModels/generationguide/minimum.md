# minimum(_:)

**Framework**: Foundation Models  
**Kind**: method

Enforces a minimum value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func minimum(_ value: Decimal) -> GenerationGuide<Decimal>
```

#### Discussion

Use a `minimum` generation guide — whose bounds are inclusive — to ensure the model produces a value greater than or equal to some minimum value. For example, you can specify that all characters in your game start at level 1:

```swift
@Generable
struct GameCharacter {
    @Guide(description: "A creative name appropriate for a fantasy RPG character")
    var name: String

    @Guide(description: "A level for the character", .minimum(1))
    var level: Int
}
```

## See Also

- [static func minimumCount<Element>(Int) -> GenerationGuide<[Element]>](generationguide/minimumcount(_:).md)
  Enforces a minimum number of elements in the array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationguide/minimum(_:))*