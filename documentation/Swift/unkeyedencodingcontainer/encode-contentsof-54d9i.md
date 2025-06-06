# encode(contentsOf:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Encodes the elements of the given sequence.

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
mutating func encode<T>(contentsOf sequence: T) throws where T : Sequence, T.Element == Bool
```

#### Discussion

> **Note**: An error if any of the contained values throws an error.

## Parameters

- `sequence`: The sequences whose contents to encode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encode(contentsof:)-54d9i)*