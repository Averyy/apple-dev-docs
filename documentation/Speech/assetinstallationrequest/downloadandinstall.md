# downloadAndInstall()

**Framework**: Speech  
**Kind**: method

Downloads and installs assets not already on the device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func downloadAndInstall() async throws
```

#### Discussion

If the system is unable to immediately download assets because of a connectivity issue or other error, the system will automatically attempt to download the assets later. This method will return when the initial download and installation attempt has succeeded or failed; use [`status(forModules:)`](assetinventory/status(formodules:).md) or another installation request to monitor the success or progress of later attempts.

The system consolidates download and installation requests; you may call this method several times without causing redundant downloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/assetinstallationrequest/downloadandinstall())*