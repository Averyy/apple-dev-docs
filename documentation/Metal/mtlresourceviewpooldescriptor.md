# MTLResourceViewPoolDescriptor

**Framework**: Metal  
**Kind**: class

Provides parameters for creating a resource view pool.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class MTLResourceViewPoolDescriptor
```

## Topics

### Instance Properties
- [var label: String?](mtlresourceviewpooldescriptor/label.md)
  Assigns an optional label you to the resource view pool for debugging purposes.
- [var resourceViewCount: Int](mtlresourceviewpooldescriptor/resourceviewcount.md)
  Configures the number of resource views with which Metal creates the resource view pool.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [protocol MTLResourceViewPool](mtlresourceviewpool.md)
  Contains views over resources of a specific type, and allows you to manage those views.
- [protocol MTLTextureViewPool](mtltextureviewpool.md)
  A pool of lightweight texture views.
- [class MTLTextureViewDescriptor](mtltextureviewdescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceviewpooldescriptor)*