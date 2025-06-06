# encode(to:)

**Framework**: SwiftData  
**Kind**: method

Encodes this value into the given encoder, when the type’s `RawValue` is `String`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

#### Discussion

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/schema/relationship/deleterule-swift.enum/encode(to:))*