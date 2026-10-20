# IOSurface

**Framework**: IOSurface  
**Kind**: class  
**Role**: Class

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

```objc
@interface IOSurface : NSObject
```

## Topics

### Initializers
- [init?(properties: [IOSurfacePropertyKey : any Sendable])](./iosurface-page/init%28properties%29.md)
- [init(IOSurfaceRef)](./iosurface-page/init%28_%29.md)
- [init?(coder: NSCoder)](./iosurface-page/init%28coder%29.md)
### Instance Properties
- [var allocationSize: Int](./iosurface-page/allocationsize.md)
- [var allowsPixelSizeCasting: Bool](./iosurface-page/allowspixelsizecasting.md)
- [var baseAddress: UnsafeMutableRawPointer](./iosurface-page/baseaddress.md)
- [var bytesPerElement: Int](./iosurface-page/bytesperelement.md)
- [var bytesPerRow: Int](./iosurface-page/bytesperrow.md)
- [var elementHeight: Int](./iosurface-page/elementheight.md)
- [var elementWidth: Int](./iosurface-page/elementwidth.md)
- [var height: Int](./iosurface-page/height.md)
- [var isInUse: Bool](./iosurface-page/isinuse.md)
- [var localUseCount: Int32](./iosurface-page/localusecount.md)
- [var pixelFormat: OSType](./iosurface-page/pixelformat.md)
- [var planeCount: Int](./iosurface-page/planecount.md)
- [var seed: UInt32](./iosurface-page/seed.md)
- [var width: Int](./iosurface-page/width.md)
- [var surfaceID: UInt32](./iosurface-page/surfaceid.md)
### Instance Methods
- [func allAttachments() -> [String : any Sendable]?](./iosurface-page/allattachments%28%29.md)
- [func attachment(forKey: String) -> (any Sendable)?](./iosurface-page/attachment%28forkey%29.md)
- [func baseAddressOfPlane(at: Int) -> UnsafeMutableRawPointer](./iosurface-page/baseaddressofplane%28at%29.md)
- [func bytesPerElementOfPlane(at: Int) -> Int](./iosurface-page/bytesperelementofplane%28at%29.md)
- [func bytesPerRowOfPlane(at: Int) -> Int](./iosurface-page/bytesperrowofplane%28at%29.md)
- [func decrementUseCount()](./iosurface-page/decrementusecount%28%29.md)
- [func elementHeightOfPlane(at: Int) -> Int](./iosurface-page/elementheightofplane%28at%29.md)
- [func elementWidthOfPlane(at: Int) -> Int](./iosurface-page/elementwidthofplane%28at%29.md)
- [func heightOfPlane(at: Int) -> Int](./iosurface-page/heightofplane%28at%29.md)
- [func incrementUseCount()](./iosurface-page/incrementusecount%28%29.md)
- [func lock(options: IOSurfaceLockOptions, seed: UnsafeMutablePointer<UInt32>?) -> kern_return_t](./iosurface-page/lock%28options,seed%29.md)
- [func removeAllAttachments()](./iosurface-page/removeallattachments%28%29.md)
- [func removeAttachment(forKey: String)](./iosurface-page/removeattachment%28forkey%29.md)
- [func setAllAttachments([String : any Sendable])](./iosurface-page/setallattachments%28_%29.md)
- [func setAttachment(any Sendable, forKey: String)](./iosurface-page/setattachment%28_,forkey%29.md)
- [func setPurgeable(IOSurfacePurgeabilityState, oldState: UnsafeMutablePointer<IOSurfacePurgeabilityState>?) -> kern_return_t](./iosurface-page/setpurgeable%28_,oldstate%29.md)
- [func unlock(options: IOSurfaceLockOptions, seed: UnsafeMutablePointer<UInt32>?) -> kern_return_t](./iosurface-page/unlock%28options,seed%29.md)
- [func widthOfPlane(at: Int) -> Int](./iosurface-page/widthofplane%28at%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Classes
- [class IOSurfaceRef](./iosurfaceref.md)
  Data type representing an IOSurface opaque object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iosurface/iosurface)*