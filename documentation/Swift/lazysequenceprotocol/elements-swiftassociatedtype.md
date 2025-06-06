# Elements

**Framework**: Swift  
**Kind**: associatedtype  
**Required**: Yes

A `Sequence` that can contain the same elements as this one, possibly with a simpler type.

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
associatedtype Elements : Sequence = Self where Self.Element == Self.Elements.Element
```

#### Discussion

- See also: `elements`


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazysequenceprotocol/elements-swift.associatedtype)*