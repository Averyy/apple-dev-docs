# error

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An optional error object.

**Availability**:
- iOS 4.0+ - Deprecated in 18.0
- iPadOS 4.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.7+ - Deprecated in 15.0
- tvOS 9.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use `export(to:as:)` instead.

## Declaration

```swift
var error: (any Error)? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSError * error;
```

## Discussion

The default value of this property is `nil`. The export session sets it to an error object if its status changes to [`AVAssetExportSession.Status.failed`](./status-swift.enum/failed.md) or [`AVAssetExportSession.Status.cancelled`](./status-swift.enum/cancelled.md).

## See Also

### Monitoring export progress
- [status](./status-swift.property.md)
  The status of the export session.
- [progress](./progress.md)
  A value that indicates the progress of the export.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetexportsession/error)*