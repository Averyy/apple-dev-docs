# avoidSync

**Framework**: IOSurface  
**Kind**: property

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static var avoidSync: IOSurfaceLockOptions { get }
```

#### Discussion

If you want to detect/avoid a potentially expensive paging operation (such as readback from a GPU to system memory) when you lock the buffer, you may include this flag. If locking the buffer requires a readback, the lock will fail with an error return of `kIOReturnCannotLock`.

## See Also

- [static var readOnly: IOSurfaceLockOptions](iosurfacelockoptions/readonly.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iosurface/iosurfacelockoptions/avoidsync)*