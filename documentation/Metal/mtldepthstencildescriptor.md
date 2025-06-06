# MTLDepthStencilDescriptor

**Framework**: Metal  
**Kind**: class

An object that configures new [`MTLDepthStencilState`](mtldepthstencilstate.md) objects.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class MTLDepthStencilDescriptor
```

#### Overview

A [`MTLDepthStencilDescriptor`](mtldepthstencildescriptor.md) object is used to define a specific configuration of the depth and stencil stages of a rendering pipeline. To create a [`MTLDepthStencilDescriptor`](mtldepthstencildescriptor.md) object, use standard allocation and initialization techniques.

To enable writing the depth value to a depth attachment, set the depthWriteEnabled property to [`true`](https://developer.apple.com/documentation/swift/true).

The depthCompareFunction property specifies how the depth test is performed. If a fragment’s depth value fails the depth test, the fragment is discarded. [`MTLCompareFunction.less`](mtlcomparefunction/less.md) is a commonly used value for [`depthCompareFunction`](mtldepthstencildescriptor/depthcomparefunction.md), because fragment values that are farther away from the viewer than the pixel depth value (a previously written fragment) fail the depth test and are considered occluded by the earlier depth value.

The [`frontFaceStencil`](mtldepthstencildescriptor/frontfacestencil.md) and [`backFaceStencil`](mtldepthstencildescriptor/backfacestencil.md) properties define two independent stencil descriptors: one for front-facing primitives and the other for back-facing primitives, respectively. Both properties can be set to the same MTLStencilDescriptor object.

## Topics

### Specifying Depth Operations
- [var depthCompareFunction: MTLCompareFunction](mtldepthstencildescriptor/depthcomparefunction.md)
  The comparison that is performed between a fragment’s depth value and the depth value in the attachment, which determines whether to discard the fragment.
- [var isDepthWriteEnabled: Bool](mtldepthstencildescriptor/isdepthwriteenabled.md)
  A Boolean value that indicates whether depth values can be written to the depth attachment.
### Specifying Stencil Descriptors for Primitives
- [var backFaceStencil: MTLStencilDescriptor!](mtldepthstencildescriptor/backfacestencil.md)
  The stencil descriptor for back-facing primitives.
- [var frontFaceStencil: MTLStencilDescriptor!](mtldepthstencildescriptor/frontfacestencil.md)
  The stencil descriptor for front-facing primitives.
### Identifying Properties
- [var label: String?](mtldepthstencildescriptor/label.md)
  A string that identifies this object.

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

- [Calculating Primitive Visibility Using Depth Testing](calculating-primitive-visibility-using-depth-testing.md)
  Determine which pixels are visible in a scene by using a depth texture.
- [protocol MTLDepthStencilState](mtldepthstencilstate.md)
  A depth and stencil state object that specifies the depth and stencil configuration and operations used in a render pass.
- [class MTLStencilDescriptor](mtlstencildescriptor.md)
  An object that defines the front-facing or back-facing stencil operations of a depth and stencil state object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldepthstencildescriptor)*