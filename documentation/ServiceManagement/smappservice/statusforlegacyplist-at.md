# statusForLegacyPlist(at:)

**Framework**: Service Management  
**Kind**: method

Check the authorization status of an earlier OS version login item.

**Availability**:
- Mac Catalyst 16.0+
- macOS 13.0+

## Declaration

```swift
class func statusForLegacyPlist(at url: URL) -> SMAppService.Status
```

## Mentions

- [Updating helper executables from earlier versions of macOS](updating-helper-executables-from-earlier-versions-of-macos.md)

#### Return Value

One of the [`SMAppService.Status`](smappservice/status-swift.enum.md) constants that indicate the current authorization status.

## Parameters

- `url`: The URL of the helper executable’s property list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/servicemanagement/smappservice/statusforlegacyplist(at:))*