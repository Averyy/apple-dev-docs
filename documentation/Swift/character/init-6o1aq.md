# init(_:)

**Framework**: Swift  
**Kind**: init

Creates a character from a single-character string.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(_ s: String)
```

#### Discussion

The following example creates a new character from the uppercase version of a string that only holds one character.

```swift
let a = "a"
let capitalA = Character(a.uppercased())
```

## Parameters

- `s`: The single-character string to convert to a    instance.   must contain exactly one extended grapheme cluster.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character/init(_:)-6o1aq)*