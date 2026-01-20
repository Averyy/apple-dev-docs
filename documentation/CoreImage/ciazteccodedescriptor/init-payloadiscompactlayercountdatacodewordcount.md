# init(payload:isCompact:layerCount:dataCodewordCount:)

**Framework**: Core Image  
**Kind**: init

Initializes an Aztec code descriptor for the given payload and parameters.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init?(payload errorCorrectedPayload: Data, isCompact: Bool, layerCount: Int, dataCodewordCount: Int)
```

#### Return Value

 An initialized [`CIAztecCodeDescriptor`](ciazteccodedescriptor.md) instance or `nil` if the parameters are invalid

## Parameters

- `errorCorrectedPayload`: The data to encode in the Aztec code symbol.
- `isCompact`: A Boolean indicating whether or not the Aztec code is compact.
- `layerCount`: The number of layers in the Aztec code, from 1 to 32.
- `dataCodewordCount`: The number of codewords in the Aztec code, from 1 to 2048.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor/init(payload:iscompact:layercount:datacodewordcount:))*