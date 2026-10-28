# notRecognized

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

A probe result for an unrecognized file system.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class var notRecognized: FSProbeResult { get }
```

```objc
@property (class, readonly) FSProbeResult * notRecognizedProbeResult;
```

## Discussion

An unrecognized probe result contains `nil` for its [`name`](./name.md) and [`containerID`](./containerid.md) properties.

## See Also

### Working with results
- [class func recognized(name: String, containerID: FSContainerIdentifier) -> Self](./recognized%28name,containerid%29.md)
  Creates a probe result for a recognized file system.
- [class func usable(name: String, containerID: FSContainerIdentifier) -> Self](./usable%28name,containerid%29.md)
  Creates a probe result for a recognized and usable file system.
- [class func usableButLimited(name: String, containerID: FSContainerIdentifier) -> Self](./usablebutlimited%28name,containerid%29.md)
  Creates a probe result for a recognized file system that is usable, but with limited capabilities.
- [class var usableButLimited: FSProbeResult](./usablebutlimited.md)
  A probe result for a recognized file system that is usable, but with limited capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsproberesult/notrecognized)*