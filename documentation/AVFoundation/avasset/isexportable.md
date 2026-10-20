# isExportable

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you can export this asset using an export session.

**Availability**:
- iOS 4.3+ - Deprecated in 16.0
- iPadOS 4.3+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0

> **Deprecated**: Load the value of [`isExportable`](../avpartialasyncproperty/isexportable.md) asynchronously instead.

## Declaration

```swift
var isExportable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isExportable) BOOL exportable;
```

#### Discussion

This property value is [`true`](../../Swift/true.md) if you can export the asset using [`AVAssetExportSession`](../avassetexportsession.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/isexportable)*