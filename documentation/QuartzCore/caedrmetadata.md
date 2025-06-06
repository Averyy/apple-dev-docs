# CAEDRMetadata

**Framework**: Core Animation  
**Kind**: class

Metadata describing how extended dynamic range (EDR) values should be tone mapped.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class CAEDRMetadata
```

#### Overview

If you need specific tone-mapping behavior, set the [`edrMetadata`](cametallayer/edrmetadata.md) property of a [`CAMetalLayer`](cametallayer.md) to point to an instance of this class.

## Topics

### Retrieving Hybrid-Log Gamma Metadata
- [class var hlg: CAEDRMetadata](caedrmetadata/hlg.md)
  Extended dynamic range (EDR) metadata for the Hybrid Log-Gamma (HLG) transfer function.
### Retrieving HDR10 Metadata
- [class func hdr10(displayInfo: Data?, contentInfo: Data?, opticalOutputScale: Float) -> CAEDRMetadata](caedrmetadata/hdr10(displayinfo:contentinfo:opticaloutputscale:).md)
  Creates EDR metadata for HDR10 content based on mastering display color information and content light levels.
- [class func hdr10(minLuminance: Float, maxLuminance: Float, opticalOutputScale: Float) -> CAEDRMetadata](caedrmetadata/hdr10(minluminance:maxluminance:opticaloutputscale:).md)
  Creates EDR metadata for HDR10 content based on the luminance characteristics of a mastering display.
### Type Properties
- [class var isAvailable: Bool](caedrmetadata/isavailable.md)
### Type Methods
- [class func hlg(ambientViewingEnvironment: Data) -> CAEDRMetadata](caedrmetadata/hlg(ambientviewingenvironment:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
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

## See Also

- [class CAMetalLayer](cametallayer.md)
  A Core Animation layer that Metal can render into, typically displayed onscreen.
- [protocol CAMetalDrawable](cametaldrawable.md)
  A Metal drawable associated with a Core Animation layer.
- [class CAEAGLLayer](caeagllayer.md)
  A layer that supports drawing OpenGL content in iOS and tvOS applications.
- [class CAOpenGLLayer](caopengllayer.md)
  A layer that provides a layer suitable for rendering OpenGL content.
- [class CARenderer](carenderer.md)
  A layer that allows an application to render a layer tree into a Core OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caedrmetadata)*