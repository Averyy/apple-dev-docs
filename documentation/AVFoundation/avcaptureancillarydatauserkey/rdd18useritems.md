# rdd18UserItems

**Framework**: AVFoundation  
**Kind**: property

An AVCaptureAncillaryDataEncoder key corresponding with RDD18 user defined metadata

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
static let rdd18UserItems: AVCaptureAncillaryDataUserKey
```

#### Discussion

Clients may inspect the user metadata with `AVCaptureAncillaryDataEncoder\currentUserDefinedAncillaryData` and set it with `AVCaptureAncillaryDataEncoder\setRDD18AncillaryData:forTag:error:` `AVCaptureAncillaryDataEncoder\setRDD18AncillaryDataString:forTag:error:` or remove it with `AVCaptureAncillaryDataEncoder\removeRDD18AncillaryDataForTag:`


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureancillarydatauserkey/rdd18useritems)*