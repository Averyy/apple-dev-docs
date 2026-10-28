# init(items:timeRange:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a timed metadata group initialized with the given metadata items.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
init(items: [AVMetadataItem], timeRange: CMTimeRange)
```

```objc
- (instancetype) initWithItems:(NSArray<AVMetadataItem *> *) items timeRange:(CMTimeRange) timeRange;
```

## Return Value

A metadata group initialized with `items`.

## Parameters

- `items`: An array of [`AVMetadataItem`](../avmetadataitem.md) objects.
- `timeRange`: The time range of the metadata contained in `items`.

## See Also

### Creating a timed metadata group
- [convenience init?(sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>)](./init%28samplebuffer%29-6atlv.md)
  Creates a timed metadata group with a sample buffer.
- [init?(sampleBuffer: CMSampleBuffer)](./init%28samplebuffer%29-bjuo.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/init(items:timerange:))*