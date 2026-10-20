# NSURLHandle.Status

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

These following constants are defined by `NSURLHandle` and are returned by [`status`](./status-c.method.md).

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
enum Status
```

```c
enum NSURLHandleStatus : NSUInteger;
```

## Topics

### Constants
- [NSURLHandle.Status.notLoaded](./status-swift.enum/notloaded.md)
  The resource data has not been loaded.
- [NSURLHandle.Status.loadSucceeded](./status-swift.enum/loadsucceeded.md)
  The resource data was successfully loaded.
- [NSURLHandle.Status.loadInProgress](./status-swift.enum/loadinprogress.md)
  The resource data is in the process of loading.
- [NSURLHandle.Status.loadFailed](./status-swift.enum/loadfailed.md)
  The resource data failed to load.
### Initializers
- [init?(rawValue: UInt)](./status-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsurlhandle/status-swift.enum)*