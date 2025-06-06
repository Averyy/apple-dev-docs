# NSURLHandle

**Framework**: Foundation  
**Kind**: class

An object that accesses and manages resource data indicated by a URL.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class NSURLHandle
```

#### Overview

> ❗ **Important**:  [`NSURLHandle`](nsurlhandle.md) is deprecated in macOS 10.4 and later. Use [`URLSession`](urlsession.md) instead.

 [`NSURLHandle`](nsurlhandle.md) is deprecated in macOS 10.4 and later. Use [`URLSession`](urlsession.md) instead.

A single [`NSURLHandle`](nsurlhandle.md) can service multiple equivalent [`NSURL`](nsurl.md) objects, but only if these URLs map to the same resource.

##### Overview

Cocoa provides private concrete subclasses to handle HTTP and file URL schemes. If you want to implement support for additional URL schemes, you would do so by creating a subclass of `NSURLHandle`. You can use `NSURL` and `NSURLHandle` to download from FTP sites without subclassing.

## Topics

### Loading resource data
- [NSURLHandle.Status](nsurlhandle/status-swift.enum.md)
  These following constants are defined by `NSURLHandle` and are returned by [`status`](nsurlhandle/status-c.method.md).

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandle)*