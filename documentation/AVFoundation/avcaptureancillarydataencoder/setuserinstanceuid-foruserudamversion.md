# setUserInstanceUID(_:forUserUDAMVersion:)

**Framework**: AVFoundation  
**Kind**: method

Set the UID and Version number for the user data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
func setUserInstanceUID(_ uuid: UUID, forUserUDAMVersion version: NSNumber)
```

#### Discussion

Allows the user to set the instance and version of the ancillary data.

## Parameters

- `uuid`: The UUID for the SMPTE RDD 18 ancillary data instance
- `version`: The SMPTE RDD 18 User Defined Acquisition Metadata (UDAM) Set Version


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureancillarydataencoder/setuserinstanceuid(_:foruserudamversion:))*