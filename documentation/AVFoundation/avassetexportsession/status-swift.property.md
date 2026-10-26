# status

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The status of the export session.

**Availability**:
- iOS 4.0+ - Deprecated in 18.0
- iPadOS 4.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use [`states(updateInterval:)`](./states%28updateinterval%29.md) instead.

## Declaration

```swift
var status: AVAssetExportSession.Status { get }
```

```objc
@property (nonatomic, readonly) AVAssetExportSessionStatus status;
```

#### Discussion

For possible values, see [`AVAssetExportSession.Status`](./status-swift.enum.md).

This value is key-value observable.

## See Also

### Monitoring export progress
- [progress](./progress.md)
  A value that indicates the progress of the export.
- [error](./error.md)
  An optional error object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/status-swift.property)*