# items

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

An array of metadata items in the timed metadata group.

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
var items: [AVMetadataItem] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<AVMetadataItem *> * items;
```

#### Discussion

The array contains instances of [`AVMetadataItem`](../avmetadataitem.md).

## See Also

### Accessing group attributes
- [var timeRange: CMTimeRange](./timerange.md)
  The time range for the timed metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/items)*