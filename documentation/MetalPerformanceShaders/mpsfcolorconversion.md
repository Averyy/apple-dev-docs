# MPSFColorConversion

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class MPSFColorConversion
```

```objc
@interface MPSFColorConversion : MPSFunction
```

## Topics

### Initializers
- [init(device: any MTLDevice, conversion: CGColorConversionInfo?, functionName: String, sourceRange: UnsafePointer<MPSFunctions_AABB>?, options: MPSFColorConversionOptions) throws](./mpsfcolorconversion/init%28device,conversion,functionname,sourcerange,options%29.md)
- [convenience init(device: any MTLDevice, start: CGColorSpace, end: CGColorSpace, functionName: String, sourceRange: UnsafePointer<MPSFunctions_AABB>?, options: MPSFColorConversionOptions) throws](./mpsfcolorconversion/init%28device,start,end,functionname,sourcerange,options%29.md)
- [convenience init(device: any MTLDevice, startColorSpace: CGColorSpace, endColorSpace: CGColorSpace, functionName: String, sourceRange: UnsafePointer<MPSFunctions_AABB>?, options: MPSFColorConversionOptions) throws](./mpsfcolorconversion/init%28device,startcolorspace,endcolorspace,functionname,sourcerange,options%29.md)
### Instance Properties
- [var inputColorChannels: Int](./mpsfcolorconversion/inputcolorchannels.md)
- [var options: MPSFColorConversionOptions](./mpsfcolorconversion/options.md)
- [var outputColorChannels: Int](./mpsfcolorconversion/outputcolorchannels.md)
### Instance Methods
- [func descriptorFor1DTexture1() -> MTLTextureDescriptor?](./mpsfcolorconversion/descriptorfor1dtexture1%28%29.md)
- [func descriptorFor3DTexture1() -> MTLTextureDescriptor?](./mpsfcolorconversion/descriptorfor3dtexture1%28%29.md)
- [func descriptorFor3DTexture2() -> MTLTextureDescriptor?](./mpsfcolorconversion/descriptorfor3dtexture2%28%29.md)
- [func effectiveRange(MPSFunctions_AABB) -> MPSFunctions_AABB](./mpsfcolorconversion/effectiverange%28_%29.md)
- [func initialize1DTexture1((any MTLTexture)?)](./mpsfcolorconversion/initialize1dtexture1%28_%29.md)
- [func initialize3DTexture1((any MTLTexture)?)](./mpsfcolorconversion/initialize3dtexture1%28_%29.md)
- [func initialize3DTexture2((any MTLTexture)?)](./mpsfcolorconversion/initialize3dtexture2%28_%29.md)

## Relationships

### Inherits From
- [MPSFunction](./mpsfunction.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsfcolorconversion)*