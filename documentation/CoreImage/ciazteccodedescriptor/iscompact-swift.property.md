# isCompact

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

A Boolean value telling if the Aztec code is compact.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var isCompact: Bool { get }
```

```objc
@property (readonly) BOOL isCompact;
```

#### Discussion

Compact Aztec symbols use one-fewer ring in the central finder pattern than full-range Aztec symbols of the same number of data layers.

## See Also

### Examining a Descriptor
- [var errorCorrectedPayload: Data](./errorcorrectedpayload-swift.property.md)
  The error-corrected payload that comprises the the Aztec code symbol.
- [var layerCount: Int](./layercount-swift.property.md)
  The number of data layers in the Aztec code symbol.
- [var dataCodewordCount: Int](./datacodewordcount-swift.property.md)
  The number of non-error-correction codewords carried by the Aztec code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor/iscompact-swift.property)*