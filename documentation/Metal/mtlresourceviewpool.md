# MTLResourceViewPool

**Framework**: Metal  
**Kind**: protocol

Contains views over resources of a specific type, and allows you to manage those views.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol MTLResourceViewPool : NSObjectProtocol
```

## Topics

### Instance Properties
- [var baseResourceID: MTLResourceID](mtlresourceviewpool/baseresourceid.md)
  Obtains the resource ID corresponding to the resource view at index 0 in this resource view pool.
- [var device: any MTLDevice](mtlresourceviewpool/device.md)
  Obtains a reference to the GPU device this pool belongs to.
- [var label: String?](mtlresourceviewpool/label.md)
  Queries the optional debug label of this resource view pool.
- [var resourceViewCount: Int](mtlresourceviewpool/resourceviewcount.md)
  Queries the number of resource views that this pool contains.
### Instance Methods
- [func copyResourceViews(sourcePool: any MTLResourceViewPool, sourceRange: Range<Int>, destinationIndex: Int) -> MTLResourceID](mtlresourceviewpool/copyresourceviews(sourcepool:sourcerange:destinationindex:).md)
  Copies a range of resource views from a source view pool to a destination location in this view pool.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [MTLTextureViewPool](mtltextureviewpool.md)

## See Also

- [class MTLResourceViewPoolDescriptor](mtlresourceviewpooldescriptor.md)
  Provides parameters for creating a resource view pool.
- [protocol MTLTextureViewPool](mtltextureviewpool.md)
  A pool of lightweight texture views.
- [class MTLTextureViewDescriptor](mtltextureviewdescriptor.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlresourceviewpool)*