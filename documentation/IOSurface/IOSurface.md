# IOSurface

**Framework**: IOSurface  
**Kind**: module

Share hardware-accelerated buffer data (framebuffers and textures) across multiple processes. Manage image memory more efficiently.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 11.0+
- visionOS 1.0+

#### Overview

The IOSurface framework provides a framebuffer object suitable for sharing across process boundaries. It is commonly used to allow applications to move complex image decompression and draw logic into a separate process to enhance security.

## Topics

### Classes
- [class IOSurface](iosurface.md)
  Data type representing an IOSurface opaque object.
- [class IOSurfaceRef](iosurfaceref.md)
  Data type representing an IOSurface opaque object.
### Structures
- [struct IOSurfaceLockOptions](iosurfacelockoptions.md)
- [struct IOSurfacePropertyKey](iosurfacepropertykey.md)
- [struct IOSurfacePurgeabilityState](iosurfacepurgeabilitystate.md)
### Reference
- [IOSurface Structures](iosurface-structures.md)
- [IOSurface Constants](iosurface-constants.md)
- [IOSurface Functions](iosurface-functions.md)
### Variables
- [let kIOSurfaceContentHeadroom: CFString](kiosurfacecontentheadroom.md)
- [var kIOSurfaceCopybackCache: Int](kiosurfacecopybackcache.md)
- [var kIOSurfaceCopybackInnerCache: Int](kiosurfacecopybackinnercache.md)
- [var kIOSurfaceDefaultCache: Int](kiosurfacedefaultcache.md)
- [var kIOSurfaceInhibitCache: Int](kiosurfaceinhibitcache.md)
- [var kIOSurfaceMapCacheShift: Int](kiosurfacemapcacheshift.md)
- [var kIOSurfaceMapCopybackCache: Int](kiosurfacemapcopybackcache.md)
- [var kIOSurfaceMapCopybackInnerCache: Int](kiosurfacemapcopybackinnercache.md)
- [var kIOSurfaceMapDefaultCache: Int](kiosurfacemapdefaultcache.md)
- [var kIOSurfaceMapInhibitCache: Int](kiosurfacemapinhibitcache.md)
- [var kIOSurfaceMapWriteCombineCache: Int](kiosurfacemapwritecombinecache.md)
- [var kIOSurfaceMapWriteThruCache: Int](kiosurfacemapwritethrucache.md)
- [var kIOSurfaceWriteCombineCache: Int](kiosurfacewritecombinecache.md)
- [var kIOSurfaceWriteThruCache: Int](kiosurfacewritethrucache.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/IOSurface)*