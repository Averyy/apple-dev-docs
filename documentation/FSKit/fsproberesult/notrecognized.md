# notRecognized

**Framework**: FSKit  
**Kind**: property

A probe result for an unrecognized file system.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class var notRecognized: FSProbeResult { get }
```

#### Discussion

An unrecognized probe result contains `nil` for its [`name`](fsproberesult/name.md) and [`containerID`](fsproberesult/containerid.md) properties.

## See Also

- [class func recognized(name: String, containerID: FSContainerIdentifier) -> Self](fsproberesult/recognized(name:containerid:).md)
  Creates a probe result for a recognized file system.
- [class func usable(name: String, containerID: FSContainerIdentifier) -> Self](fsproberesult/usable(name:containerid:).md)
  Creates a probe result for a recognized and usable file system.
- [class func usableButLimited(name: String, containerID: FSContainerIdentifier) -> Self](fsproberesult/usablebutlimited(name:containerid:).md)
  Creates a probe result for a recognized file system that is usable, but with limited capabilities.
- [class var usableButLimited: FSProbeResult](fsproberesult/usablebutlimited.md)
  A probe result for a recognized file system that is usable, but with limited capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsproberesult/notrecognized)*