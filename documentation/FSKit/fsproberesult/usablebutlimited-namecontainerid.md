# usableButLimited(name:containerID:)

**Framework**: FSKit  
**Kind**: method

Creates a probe result for a recognized file system that is usable, but with limited capabilities.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class func usableButLimited(name: String, containerID: FSContainerIdentifier) -> Self
```

## Parameters

- `name`: The resource name, as found during the probe operation. If the file system doesn’t support names, or is awaiting naming, use an empty string.
- `containerID`: The container identifier, as found during the probe operation. If the file system doesn’t support durable identifiers, use a random UUID.

## See Also

- [class func recognized(name: String, containerID: FSContainerIdentifier) -> Self](fsproberesult/recognized(name:containerid:).md)
  Creates a probe result for a recognized file system.
- [class func usable(name: String, containerID: FSContainerIdentifier) -> Self](fsproberesult/usable(name:containerid:).md)
  Creates a probe result for a recognized and usable file system.
- [class var usableButLimited: FSProbeResult](fsproberesult/usablebutlimited.md)
  A probe result for a recognized file system that is usable, but with limited capabilities.
- [class var notRecognized: FSProbeResult](fsproberesult/notrecognized.md)
  A probe result for an unrecognized file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsproberesult/usablebutlimited(name:containerid:))*