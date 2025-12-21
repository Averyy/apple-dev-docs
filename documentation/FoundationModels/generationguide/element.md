# element(_:)

**Framework**: Foundation Models  
**Kind**: method

Enforces a guide on the elements within the array.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func element<Element>(_ guide: GenerationGuide<Element>) -> GenerationGuide<[Element]> where Value == [Element]
```

#### Discussion

An `element` generation guide may be used when you want to apply guides to the values a model produces within an array. For example, you may want to generate an array of integers, where all the integers are in the range 0-9.

```swift
@Generable
struct struct FortuneCookie {
    @Guide(description: "A fortune from a fortune cookie"
    var name: String

    @Guide(description: "A list lucky numbers", .element(.range(0...9)), .count(4))
    var luckyNumbers: [Int]
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/generationguide/element(_:))*