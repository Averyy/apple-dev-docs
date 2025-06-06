# decodeIfPresent(_:)

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Decodes a value of the given type, if present.

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
mutating func decodeIfPresent(_ type: UInt32.Type) throws -> UInt32?
```

#### Return Value

A decoded value of the requested type, or `nil` if the value is a null value, or if there are no more elements to decode.

#### Discussion

This method returns `nil` if the container has no elements left to decode, or if the value is null. The difference between these states can be distinguished by checking `isAtEnd`.

> **Note**: `DecodingError.typeMismatch` if the encountered encoded value is not convertible to the requested type.

## Parameters

- `type`: The type of value to decode.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unkeyeddecodingcontainer/decodeifpresent(_:)-1oxo9)*