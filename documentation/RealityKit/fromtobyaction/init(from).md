# init(from:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a new instance from a decoder.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init(from decoder: any Decoder) throws
```

Available when `Value` conforms to `AnimatableData`.

## Discussion

Throws an error if reading from `decoder` fails, or if the data is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/fromtobyaction/init(from:))*