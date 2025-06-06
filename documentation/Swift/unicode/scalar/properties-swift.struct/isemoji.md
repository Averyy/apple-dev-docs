# isEmoji

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether the scalar has an emoji presentation, whether or not it is the default.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 10.2+
- macOS 10.12.2+
- tvOS 10.1+
- visionOS 1.0+
- watchOS 3.1.1+

## Declaration

```swift
var isEmoji: Bool { get }
```

#### Discussion

This property is true for scalars that are rendered as emoji by default and also for scalars that have a non-default emoji rendering when followed by U+FE0F VARIATION SELECTOR-16. This includes some scalars that are not typically considered to be emoji:

```swift
let scalars: [Unicode.Scalar] = ["😎", "$", "0"]
for s in scalars {
    print(s, "-->", s.properties.isEmoji)
}
// 😎 --> true
// $ --> false
// 0 --> true
```

The final result is true because the ASCII digits have non-default emoji presentations; some platforms render these with an alternate appearance.

Because of this behavior, testing `isEmoji` alone on a single scalar is insufficient to determine if a unit of text is rendered as an emoji; a correct test requires inspecting multiple scalars in a `Character`. In addition to checking whether the base scalar has `isEmoji == true`, you must also check its default presentation (see `isEmojiPresentation`) and determine whether it is followed by a variation selector that would modify the presentation.

This property corresponds to the “Emoji” property in the [`Unicode Standard`](https://developer.apple.comhttp://www.unicode.org/versions/latest/).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar/properties-swift.struct/isemoji)*