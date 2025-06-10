# getBytes(_:strides:sliceOrigin:sliceDimensions:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Copies the data corresponding to a slice of this tensor into a pointer you provide.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func getBytes(_ bytes: UnsafeMutableRawPointer, strides: MTLTensorExtents, sliceOrigin: MTLTensorExtents, sliceDimensions: MTLTensorExtents)
```

## Parameters

- `bytes`: A pointer to bytes of data that this method copies into the slice you specify with   and  .
- `strides`: An array of strides, in elements, that describes the layout of the data in  . You are responsible for ensuring   meets the following requirements:
- `sliceOrigin`: An array of offsets, in elements, to the first element of the slice that this method reads data from.
- `sliceDimensions`: An array of sizes, in elements, of the slice this method reads data from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtltensor/getbytes(_:strides:sliceorigin:slicedimensions:))*