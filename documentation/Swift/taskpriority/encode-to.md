# encode(to:)

**Framework**: Swift  
**Kind**: method

Encodes this value into the given encoder, when the type’s `RawValue` is `UInt8`.

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
func encode(to encoder: any Encoder) throws
```

#### Discussion

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/taskpriority/encode(to:))*