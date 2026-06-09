# remainingCapacity

**Framework**: AVFoundation  
**Kind**: property

Current size of Pro Video Storage in bytes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)

## Declaration

```swift
var remainingCapacity: Int { get }
```

#### Return Value

0 if Pro Video Storage is not configured or -1 if there was a failure while extracting information from it.

#### Discussion

The remaining capacity decreases as recordings are captured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avprovideostorage/remainingcapacity)*