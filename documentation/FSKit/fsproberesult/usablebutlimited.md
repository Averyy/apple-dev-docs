# usableButLimited

**Framework**: FSKit  
**Kind**: property  
**Role**: Type Property

A probe result for a recognized file system that is usable, but with limited capabilities.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class var usableButLimited: FSProbeResult { get }
```

```objc
@property (class, readonly) FSProbeResult * usableButLimitedProbeResult;
```

## Discussion

This kind of probe result lacks the [`name`](./name.md), [`containerID`](./containerid.md), or both. Don’t return this result from probing a resource that isn’t limited.

## See Also

### Working with results
- [class func recognized(name: String, containerID: FSContainerIdentifier) -> Self](./recognized%28name,containerid%29.md)
  Creates a probe result for a recognized file system.
- [class func usable(name: String, containerID: FSContainerIdentifier) -> Self](./usable%28name,containerid%29.md)
  Creates a probe result for a recognized and usable file system.
- [class func usableButLimited(name: String, containerID: FSContainerIdentifier) -> Self](./usablebutlimited%28name,containerid%29.md)
  Creates a probe result for a recognized file system that is usable, but with limited capabilities.
- [class var notRecognized: FSProbeResult](./notrecognized.md)
  A probe result for an unrecognized file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsproberesult/usablebutlimited)*