# PhotogrammetrySession.Error.insufficientStorage(requiredBytes:)

**Framework**: RealityKit  
**Kind**: case

An error that indicates insufficient storage space.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
case insufficientStorage(requiredBytes: Int64)
```

#### Discussion

This error occurs when there is not enough available storage, and the system estimates that it needs `requiredBytes` of storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/photogrammetrysession/error/insufficientstorage(requiredbytes:))*