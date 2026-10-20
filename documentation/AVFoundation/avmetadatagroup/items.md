# items

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The array of metadata items associated with the metadata group.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var items: [AVMetadataItem] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<AVMetadataItem *> * items;
```

#### Discussion

The `items` array may be empty if no metadata items are associated with this group.

## See Also

### Inspecting the metadata group
- [var uniqueID: String?](./uniqueid.md)
  The unique identifier for the metadata group.
- [var classifyingLabel: String?](./classifyinglabel.md)
  The classifying label associated with the metadata group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatagroup/items)*