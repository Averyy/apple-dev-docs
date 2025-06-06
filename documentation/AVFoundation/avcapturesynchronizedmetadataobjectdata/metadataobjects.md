# metadataObjects

**Framework**: AVFoundation  
**Kind**: property

The list of metadata objects captured at this synchronization timestamp.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var metadataObjects: [AVMetadataObject] { get }
```

#### Discussion

> **Note**:  Because [`AVMetadataObject`](avmetadataobject.md) is an abstract class, the objects in this array are always instances of a concrete subclass.

 Because [`AVMetadataObject`](avmetadataobject.md) is an abstract class, the objects in this array are always instances of a concrete subclass.

This array is equivalent to that provided by the [`metadataOutput(_:didOutput:from:)`](avcapturemetadataoutputobjectsdelegate/metadataoutput(_:didoutput:from:).md) delegate method when using a metadata capture output without a data output synchronizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturesynchronizedmetadataobjectdata/metadataobjects)*