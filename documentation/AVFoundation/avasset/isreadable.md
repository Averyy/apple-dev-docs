# isReadable

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether you can extract the asset’s media data using an asset reader.

**Availability**:
- iOS 4.3+ - Deprecated in 16.0
- iPadOS 4.3+ - Deprecated in 16.0
- Mac Catalyst 13.1+ - Deprecated in 16.0
- macOS 10.7+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0

> **Deprecated**: Load the value of [`isReadable`](../avpartialasyncproperty/isreadable.md) asynchronously instead.

## Declaration

```swift
var isReadable: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isReadable) BOOL readable;
```

#### Discussion

This property value is [`true`](../../Swift/true.md) if you can use [`AVAssetReader`](../avassetreader.md) to extract the asset’s media data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avasset/isreadable)*