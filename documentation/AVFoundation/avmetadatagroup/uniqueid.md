# uniqueID

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The unique identifier for the metadata group.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- macOS 10.11.3+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.3+

## Declaration

```swift
var uniqueID: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * uniqueID;
```

## Discussion

The value of this property may be `nil` if no unique identifier is defined for this group.

## See Also

### Inspecting the metadata group
- [var items: [AVMetadataItem]](./items.md)
  The array of metadata items associated with the metadata group.
- [var classifyingLabel: String?](./classifyinglabel.md)
  The classifying label associated with the metadata group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadatagroup/uniqueid)*