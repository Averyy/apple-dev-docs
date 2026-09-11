# resourceStatus(for:)

**Framework**: Cinematic  
**Kind**: method

Check status for a set of resources.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst ?+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
static func resourceStatus(for versions: Set<CNCinematicResourceVersion> = []) -> CNResourceStatus
```

#### Return Value

Returns the first encountered non-ready status, or `.ready` if all are ready.

## Parameters

- `versions`: Resource version(s) to check. Empty set to check all available resource versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cinematic/cnassetinfo-2ata2/resourcestatus(for:))*