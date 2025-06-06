# HKMetadataKeyAppleECGAlgorithmVersion

**Framework**: HealthKit  
**Kind**: var

A key for metadata indicating the version number of the algorithm Apple Watch uses to generate an ECG reading.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
let HKMetadataKeyAppleECGAlgorithmVersion: String
```

#### Discussion

Apple Watch sets this key on the [`HKElectrocardiogram`](hkelectrocardiogram.md) samples it creates. The key is read-only.

## See Also

- [enum HKAppleECGAlgorithmVersion](hkappleecgalgorithmversion.md)
  Version numbers for the algorithm Apple Watch uses to generate an ECG reading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyappleecgalgorithmversion)*