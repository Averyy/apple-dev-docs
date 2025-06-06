# Regions

**Framework**: Foundation  
**Kind**: associatedtype  
**Required**: Yes

A type that represents a collection of contiguous parts that make up the type conforming to a data protocol.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
associatedtype Regions : BidirectionalCollection where Self.Regions.Element : ContiguousBytes, Self.Regions.Element : DataProtocol, Self.Regions.Element.SubSequence : ContiguousBytes
```

## See Also

- [var regions: Self.Regions](dataprotocol/regions-swift.property.md)
  A collection of buffers that make up the whole of the type conforming to a data protocol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/dataprotocol/regions-swift.associatedtype)*