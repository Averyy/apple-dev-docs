# encode(to:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Encodes this value into the given encoder.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 2.4+

## Declaration

```swift
func encode(to encoder: any Encoder) throws
```

#### Discussion

If the value fails to encode anything, `encoder` will encode an empty keyed container in its place.

This function throws an error if any values are invalid for the given encoder’s format.

## Parameters

- `encoder`: The encoder to write data to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappdistributionerror/encode(to:))*