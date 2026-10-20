# init(opaque:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Creates a new description of the conversion from YpCbCr to ARGB from the specfied bytes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
init(opaque: (UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8, UInt8))
```

#### Discussion

You don’t directly instantiate a [`vImage_YpCbCrToARGB`](../vimage_ypcbcrtoargb.md) struct; use [`vImageConvert_YpCbCrToARGB_GenerateConversion(_:_:_:_:_:_:)`](../vimageconvert_ypcbcrtoargb_generateconversion%28_,_,_,_,_,_%29.md) to generate a conversion matrix.

## Parameters

- `opaque`: The bytes of the opaque representation.

## See Also

### Initializers
- [init()](./init%28%29.md)
  Creates a new description of the conversion from YpCbCr to ARGB.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_ypcbcrtoargb/init(opaque:))*