# MPSStateResourceList

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

An interface for objects that define resources for Metal Performance Shaders state containers.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSStateResourceList
```

```objc
@interface MPSStateResourceList : NSObject
```

## Topics

### Initializers
- [init()](./mpsstateresourcelist/init%28%29.md)
### Instance Methods
- [func appendBuffer(Int)](./mpsstateresourcelist/appendbuffer%28_%29.md)
- [func appendTexture(MTLTextureDescriptor)](./mpsstateresourcelist/appendtexture%28_%29.md)
### Type Methods
- [+ resourceList](./mpsstateresourcelist/resourcelist.md)
- [+ resourceListWithBufferSizes:](./mpsstateresourcelist/resourcelistwithbuffersizes_.md)
- [+ resourceListWithTextureDescriptors:](./mpsstateresourcelist/resourcelistwithtexturedescriptors_.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsstateresourcelist)*