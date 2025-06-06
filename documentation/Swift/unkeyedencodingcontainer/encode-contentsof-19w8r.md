# encode(contentsOf:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Encodes the elements of the given sequence.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
mutating func encode<T>(contentsOf sequence: T) throws where T : Sequence, T.Element == Int128
```

#### Discussion

> **Note**: An error if any of the contained values throws an error.

## Parameters

- `sequence`: The sequences whose contents to encode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyedencodingcontainer/encode(contentsof:)-19w8r)*