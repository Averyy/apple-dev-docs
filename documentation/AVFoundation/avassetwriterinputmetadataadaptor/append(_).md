# append(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Appends a timed metadata group to the adaptor.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetWriter.inputMetadataReceiver(for:) instead

## Declaration

```swift
func append(_ timedMetadataGroup: AVTimedMetadataGroup) -> Bool
```

```objc
- (BOOL) appendTimedMetadataGroup:(AVTimedMetadataGroup *) timedMetadataGroup;
```

#### Return Value

[`true`](../../Swift/true.md) if the adaptor appends the group; otherwise, [`false`](../../Swift/false.md).

#### Discussion

The timing of metadata items in the output asset correspond to the time range of the timed metadata group, regardless of the values of their individual time and duration properties.

> ❗ **Important**:  Only call this method after you’ve attached the related input to the asset writer and called its [`startWriting()`](../avassetwriter/startwriting%28%29.md) method.

## Parameters

- `timedMetadataGroup`: The timed metadata group to append.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/append(_:))*