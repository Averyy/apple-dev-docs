# layerCount

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property

The number of data layers in the Aztec code symbol.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var layerCount: Int { get }
```

```objc
@property (readonly) NSInteger layerCount;
```

## Discussion

Combined with [`isCompact`](./iscompact-swift.property.md), the number of data layers determines the number of
modules in the Aztec Code symbol. Valid values range from 1 to 32. Compact symbols can have up to 4 data layers.

The number of data layers also determines the number of bits in each data codeword of the message carried by the Aztec Code symbol.

## See Also

### Examining a Descriptor
- [var errorCorrectedPayload: Data](./errorcorrectedpayload-swift.property.md)
  The error-corrected payload that comprises the the Aztec code symbol.
- [var isCompact: Bool](./iscompact-swift.property.md)
  A Boolean value telling if the Aztec code is compact.
- [var dataCodewordCount: Int](./datacodewordcount-swift.property.md)
  The number of non-error-correction codewords carried by the Aztec code symbol.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciazteccodedescriptor/layercount-swift.property)*