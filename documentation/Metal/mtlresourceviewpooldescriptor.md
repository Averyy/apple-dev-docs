# MTLResourceViewPoolDescriptor

**Framework**: Metal  
**Kind**: class

Provides parameters for creating a resource view pool.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

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
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol MTLResourceViewPool](mtlresourceviewpool.md)
  Contains views over resources of a specific type, and allows you to manage those views.
- [protocol MTLTextureViewPool](mtltextureviewpool.md)
  A pool of lightweight texture views.
- [class MTLTextureViewDescriptor](mtltextureviewdescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceviewpooldescriptor)*