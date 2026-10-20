# userDefinedAncillaryDataSizeRemaining

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Allows users to track how much data in bytes can be added to the userDefinedAncillaryData.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+

## Declaration

```swift
var userDefinedAncillaryDataSizeRemaining: Int16 { get }
```

```objc
@property (nonatomic, readonly) int16_t userDefinedAncillaryDataSizeRemaining;
```

#### Discussion

Using SMPTE 291 and SMPTE RDD 18 standards for ancillary data, this property specifies max size in bytes for the user defined portion of that data


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureancillarydataencoder/userdefinedancillarydatasizeremaining)*