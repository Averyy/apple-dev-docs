# externalStorageDevices

**Framework**: AVFoundation  
**Kind**: property

An array of external storage devices the session updates as individual devices connect or disconnect from the system.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
var externalStorageDevices: [AVExternalStorageDevice] { get }
```

#### Discussion

Your app can monitor the changes to this array with a key-value observation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalstoragedevicediscoverysession/externalstoragedevices)*