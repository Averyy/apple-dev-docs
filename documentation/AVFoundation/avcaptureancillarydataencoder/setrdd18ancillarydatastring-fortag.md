# setRDD18AncillaryDataString(_:forTag:)

**Framework**: AVFoundation  
**Kind**: method

Allows the user to add their own string to be encoded as data and transmitted using SMPTE RDD 18 standards.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
func setRDD18AncillaryDataString(_ string: String, forTag tag: UInt16) throws
```

## Parameters

- `string`: The string to be encoded as data and transmitted
- `tag`: The SMPTE RDD 18 tag with value between 0xE011 and 0xFFFF or valid tags definded in SMPTE RDD 18:2021


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureancillarydataencoder/setrdd18ancillarydatastring(_:fortag:))*