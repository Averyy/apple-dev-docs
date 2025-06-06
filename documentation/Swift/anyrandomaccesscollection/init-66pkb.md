# init(_:)

**Framework**: Swift  
**Kind**: init

Creates an `AnyRandomAccessCollection` having the same underlying collection as `other`.

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
init?(_ other: AnyCollection<Element>)
```

#### Discussion

If the underlying collection stored by `other` does not satisfy `RandomAccessCollection`, the result is `nil`.

> **Note**: O(1)

O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyrandomaccesscollection/init(_:)-66pkb)*