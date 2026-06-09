# MPSFColorConversion

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class MPSFColorConversion
```

## Topics

### Initializers
- [init(device: any MTLDevice, conversion: CGColorConversionInfo?, functionName: String, sourceRange: UnsafePointer<MPSFunctions_AABB>?, options: MPSFColorConversionOptions) throws](mpsfcolorconversion/init(device:conversion:functionname:sourcerange:options:).md)
- [convenience init(device: any MTLDevice, start: CGColorSpace, end: CGColorSpace, functionName: String, sourceRange: UnsafePointer<MPSFunctions_AABB>?, options: MPSFColorConversionOptions) throws](mpsfcolorconversion/init(device:start:end:functionname:sourcerange:options:).md)
- [convenience init(device: any MTLDevice, startColorSpace: CGColorSpace, endColorSpace: CGColorSpace, functionName: String, sourceRange: UnsafePointer<MPSFunctions_AABB>?, options: MPSFColorConversionOptions) throws](mpsfcolorconversion/init(device:startcolorspace:endcolorspace:functionname:sourcerange:options:).md)
### Instance Properties
- [var inputColorChannels: Int](mpsfcolorconversion/inputcolorchannels.md)
- [var options: MPSFColorConversionOptions](mpsfcolorconversion/options.md)
- [var outputColorChannels: Int](mpsfcolorconversion/outputcolorchannels.md)
### Instance Methods
- [func descriptorFor1DTexture1() -> MTLTextureDescriptor?](mpsfcolorconversion/descriptorfor1dtexture1.md)
- [func descriptorFor3DTexture1() -> MTLTextureDescriptor?](mpsfcolorconversion/descriptorfor3dtexture1.md)
- [func descriptorFor3DTexture2() -> MTLTextureDescriptor?](mpsfcolorconversion/descriptorfor3dtexture2.md)
- [func effectiveRange(MPSFunctions_AABB) -> MPSFunctions_AABB](mpsfcolorconversion/effectiverange(_:).md)
- [func initialize1DTexture1((any MTLTexture)?)](mpsfcolorconversion/initialize1dtexture1(_:).md)
- [func initialize3DTexture1((any MTLTexture)?)](mpsfcolorconversion/initialize3dtexture1(_:).md)
- [func initialize3DTexture2((any MTLTexture)?)](mpsfcolorconversion/initialize3dtexture2(_:).md)

## Relationships

### Inherits From
- [MPSFunction](mpsfunction.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsfcolorconversion)*