# nextTimedMetadataGroup()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Returns the next timed metadata group for the asset reader output.

**Availability**:
- iOS 8.0+ - Deprecated in 27.0
- iPadOS 8.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use AVAssetReader.outputMetadataProvider(for:) instead

## Declaration

```swift
func nextTimedMetadataGroup() -> AVTimedMetadataGroup?
```

```objc
- (AVTimedMetadataGroup *) nextTimedMetadataGroup;
```

## Return Value

A timed metadata group that represents the next logical segment of metadata from the source asset reader output.

## Discussion

This method returns `nil` after the adaptor reads all timed metadata groups from the output, or if an error occurs. When the return value is `nil`, check the asset reader’s [`status`](../avassetreader/status-swift.property.md) property to determine why it couldn’t read more samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetreaderoutputmetadataadaptor/nexttimedmetadatagroup())*