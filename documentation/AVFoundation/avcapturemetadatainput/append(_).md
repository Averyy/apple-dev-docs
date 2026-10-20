# append(_:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Provides metadata to the capture session.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
func append(_ metadata: AVTimedMetadataGroup) throws
```

```objc
- (BOOL) appendTimedMetadataGroup:(AVTimedMetadataGroup *) metadata error:(NSError **) outError;
```

## Parameters

- `metadata`: A timed group of metadata. To denote a period of no metadata, pass an empty [`AVTimedMetadataGroup`](../avtimedmetadatagroup.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput/append(_:))*