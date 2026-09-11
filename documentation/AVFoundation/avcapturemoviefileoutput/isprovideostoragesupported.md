# isProVideoStorageSupported

**Framework**: AVFoundation  
**Kind**: property

Whether this movie file output supports writing to Pro Video Storage in its current configuration.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var isProVideoStorageSupported: Bool { get }
```

#### Discussion

A value of `YES` indicates that Pro Video Storage support is enabled for this output while `NO` indicates it is not. Check this value prior to setting property usesProVideoStorage to avoid exceptions when Pro Video Storage support is not enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/isprovideostoragesupported)*