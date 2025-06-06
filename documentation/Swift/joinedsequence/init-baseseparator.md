# init(base:separator:)

**Framework**: Swift  
**Kind**: init

Creates an iterator that presents the elements of the sequences traversed by `base`, concatenated using `separator`.

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
init<Separator>(base: Base, separator: Separator) where Separator : Sequence, Separator.Element == Base.Element.Element
```

#### Discussion

> **Note**: O(`separator.count`).

O(`separator.count`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/joinedsequence/init(base:separator:))*