# GLKEffectProperty

**Framework**: GLKit  
**Kind**: class  
**Role**: Class

The abstract superclass for configuration information used in GLKit rendering effects.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class GLKEffectProperty
```

```objc
@interface GLKEffectProperty : NSObject
```

## Overview

Subclasses of [`GLKEffectProperty`](./glkeffectproperty.md) provide one or more Objective-C properties that define how that state can be configured for an effect.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [GLKEffectPropertyFog](./glkeffectpropertyfog.md)
- [GLKEffectPropertyLight](./glkeffectpropertylight.md)
- [GLKEffectPropertyMaterial](./glkeffectpropertymaterial.md)
- [GLKEffectPropertyTexture](./glkeffectpropertytexture.md)
- [GLKEffectPropertyTransform](./glkeffectpropertytransform.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Rendering Effect Parameters
- [class GLKEffectPropertyFog](./glkeffectpropertyfog.md)
  Fog drawing information for use in GLKit rendering effects.
- [class GLKEffectPropertyLight](./glkeffectpropertylight.md)
  Lighting information for use in GLKit rendering effects.
- [class GLKEffectPropertyTexture](./glkeffectpropertytexture.md)
  Texture drawing parameters for use in GLKit rendering effects.
- [class GLKEffectPropertyMaterial](./glkeffectpropertymaterial.md)
  Surface appearance properties for use in GLKit rendering effects.
- [class GLKEffectPropertyTransform](./glkeffectpropertytransform.md)
  Coordinate transform information for use in GLKit rendering effects.
- [GLKit Effects Constants](./glkit-effects-constants.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectproperty)*