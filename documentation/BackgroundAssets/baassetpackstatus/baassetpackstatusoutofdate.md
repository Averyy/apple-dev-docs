# BAAssetPackStatusOutOfDate

**Framework**: Background Assets  
**Kind**: case  
**Role**: Enumeration Case

A status value that indicates that the downloaded asset pack is out of date.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```c
BAAssetPackStatusOutOfDate
```

#### Discussion

The presence of this status value doesn’t necessarily imply that an update to the asset pack can be downloaded over the current network connection. Check for the presence of [`BAAssetPackStatusUpdateAvailable`](./baassetpackstatusupdateavailable.md) to determine whether an update can currently be downloaded.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/baassetpackstatus/baassetpackstatusoutofdate)*