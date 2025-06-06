# IOSurface

**Framework**: IOSurface  
**Kind**: class

Data type representing an IOSurface opaque object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class IOSurface
```

## Topics

### Initializers
- [init?(properties: [IOSurfacePropertyKey : Any])](iosurface/init(properties:).md)
### Instance Properties
- [var allocationSize: Int](iosurface/allocationsize.md)
- [var allowsPixelSizeCasting: Bool](iosurface/allowspixelsizecasting.md)
- [var baseAddress: UnsafeMutableRawPointer](iosurface/baseaddress.md)
- [var bytesPerElement: Int](iosurface/bytesperelement.md)
- [var bytesPerRow: Int](iosurface/bytesperrow.md)
- [var elementHeight: Int](iosurface/elementheight.md)
- [var elementWidth: Int](iosurface/elementwidth.md)
- [var height: Int](iosurface/height.md)
- [var isInUse: Bool](iosurface/isinuse.md)
- [var localUseCount: Int32](iosurface/localusecount.md)
- [var pixelFormat: OSType](iosurface/pixelformat.md)
- [var planeCount: Int](iosurface/planecount.md)
- [var seed: UInt32](iosurface/seed.md)
- [var width: Int](iosurface/width.md)
- [var surfaceID: UInt32](iosurface/surfaceid.md)
### Instance Methods
- [func allAttachments() -> [String : Any]?](iosurface/allattachments.md)
- [func attachment(forKey: String) -> Any?](iosurface/attachment(forkey:).md)
- [func baseAddressOfPlane(at: Int) -> UnsafeMutableRawPointer](iosurface/baseaddressofplane(at:).md)
- [func bytesPerElementOfPlane(at: Int) -> Int](iosurface/bytesperelementofplane(at:).md)
- [func bytesPerRowOfPlane(at: Int) -> Int](iosurface/bytesperrowofplane(at:).md)
- [func decrementUseCount()](iosurface/decrementusecount.md)
- [func elementHeightOfPlane(at: Int) -> Int](iosurface/elementheightofplane(at:).md)
- [func elementWidthOfPlane(at: Int) -> Int](iosurface/elementwidthofplane(at:).md)
- [func heightOfPlane(at: Int) -> Int](iosurface/heightofplane(at:).md)
- [func incrementUseCount()](iosurface/incrementusecount.md)
- [func lock(options: IOSurfaceLockOptions, seed: UnsafeMutablePointer<UInt32>?) -> kern_return_t](iosurface/lock(options:seed:).md)
- [func removeAllAttachments()](iosurface/removeallattachments.md)
- [func removeAttachment(forKey: String)](iosurface/removeattachment(forkey:).md)
- [func setAllAttachments([String : Any])](iosurface/setallattachments(_:).md)
- [func setAttachment(Any, forKey: String)](iosurface/setattachment(_:forkey:).md)
- [func setPurgeable(IOSurfacePurgeabilityState, oldState: UnsafeMutablePointer<IOSurfacePurgeabilityState>?) -> kern_return_t](iosurface/setpurgeable(_:oldstate:).md)
- [func unlock(options: IOSurfaceLockOptions, seed: UnsafeMutablePointer<UInt32>?) -> kern_return_t](iosurface/unlock(options:seed:).md)
- [func widthOfPlane(at: Int) -> Int](iosurface/widthofplane(at:).md)

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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class IOSurfaceRef](iosurfaceref.md)
  Data type representing an IOSurface opaque object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iosurface/iosurface)*