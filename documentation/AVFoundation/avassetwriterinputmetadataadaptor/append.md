# append(_:)

**Framework**: AVFoundation  
**Kind**: method

Appends a timed metadata group to the adaptor.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func append(_ timedMetadataGroup: AVTimedMetadataGroup) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the adaptor appends the group; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

The timing of metadata items in the output asset correspond to the time range of the timed metadata group, regardless of the values of their individual time and duration properties.

> ❗ **Important**:  Only call this method after you’ve attached the related input to the asset writer and called its [`startWriting()`](avassetwriter/startwriting().md) method.

 Only call this method after you’ve attached the related input to the asset writer and called its [`startWriting()`](avassetwriter/startwriting().md) method.

## Parameters

- `timedMetadataGroup`: The timed metadata group to append.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/append(_:))*