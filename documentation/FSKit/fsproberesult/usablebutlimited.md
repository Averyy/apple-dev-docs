# usableButLimited

**Framework**: FSKit  
**Kind**: property

A probe result for a recognized file system that is usable, but with limited capabilities.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class var usableButLimited: FSProbeResult { get }
```

#### Discussion

This kind of probe result lacks the [`name`](fsproberesult/name.md), [`containerID`](fsproberesult/containerid.md), or both. Don’t return this result from probing a resource that isn’t limited.

## See Also

- [class func recognized(name: String, containerID: FSContainerIdentifier) -> Self](fsproberesult/recognized(name:containerid:).md)
  Creates a probe result for a recognized file system.
- [class func usable(name: String, containerID: FSContainerIdentifier) -> Self](fsproberesult/usable(name:containerid:).md)
  Creates a probe result for a recognized and usable file system.
- [class func usableButLimited(name: String, containerID: FSContainerIdentifier) -> Self](fsproberesult/usablebutlimited(name:containerid:).md)
  Creates a probe result for a recognized file system that is usable, but with limited capabilities.
- [class var notRecognized: FSProbeResult](fsproberesult/notrecognized.md)
  A probe result for an unrecognized file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsproberesult/usablebutlimited)*