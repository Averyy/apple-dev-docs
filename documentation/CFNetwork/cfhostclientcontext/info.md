# info

**Framework**: CFNetwork  
**Kind**: property

An arbitrary pointer to allocated memory containing user-defined data that can be associated with the host and that is passed to the callbacks.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var info: UnsafeMutableRawPointer?
```

## See Also

- [var copyDescription: CFAllocatorCopyDescriptionCallBack?](cfhostclientcontext/copydescription.md)
  The callback used to create a descriptive string representation of the info pointer (or the data pointed to by the info pointer) for debugging purposes. This callback is called by the [`CFCopyDescription(_:)`](https://developer.apple.com/documentation/CoreFoundation/CFCopyDescription(_:)) function.
- [var release: CFAllocatorReleaseCallBack?](cfhostclientcontext/release.md)
  The callback used to remove a retain previously added for the host on the info pointer.
- [var retain: CFAllocatorRetainCallBack?](cfhostclientcontext/retain.md)
  The callback used to add a retain for the host on the info pointer for the life of the host, and may be used for temporary references the host needs to take. This callback returns the actual info pointer to store in the host, almost always just the pointer passed as the parameter.
- [var version: CFIndex](cfhostclientcontext/version.md)
  The version number of the structure type passed as a parameter to the host client function. The only valid version number is `0`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cfnetwork/cfhostclientcontext/info)*