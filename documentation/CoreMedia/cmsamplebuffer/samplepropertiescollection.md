# CMSampleBuffer.SamplePropertiesCollection

**Framework**: Core Media  
**Kind**: struct

Fixed size collection of sample information.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct SamplePropertiesCollection
```

#### Overview

This collection contains one element for each sample in the sample buffer. The size of collection is fixed to the number of samples in a sample buffer. Convenience static methods are available on timings & sizes to create this collection by specifying just one value.

## Topics

### Initializers
- [init()](cmsamplebuffer/samplepropertiescollection/init.md)
  Creates an empty collection.
- [init(some Collection<CMSampleBuffer.SampleProperties>)](cmsamplebuffer/samplepropertiescollection/init(_:).md)
- [init(sampleCount: Int, sizes: CMSampleBuffer.SizePerSample?, timings: CMSampleBuffer.TimingPerSample?, attachments: [CMSampleBuffer.SampleAttachments]?)](cmsamplebuffer/samplepropertiescollection/init(samplecount:sizes:timings:attachments:).md)
  Create a collection with specified sample information.
### Instance Properties
- [var attachments: [CMSampleBuffer.SampleAttachments]?](cmsamplebuffer/samplepropertiescollection/attachments.md)
  Access sample attachments.
- [var count: Int](cmsamplebuffer/samplepropertiescollection/count.md)
  The number of elements in the collection.
- [var endIndex: Int](cmsamplebuffer/samplepropertiescollection/endindex.md)
  The position one greater than the last valid subscript argument.
- [var sizes: CMSampleBuffer.SizePerSample?](cmsamplebuffer/samplepropertiescollection/sizes.md)
  Access sample sizes.
- [var startIndex: Int](cmsamplebuffer/samplepropertiescollection/startindex.md)
  The position of the first element.
- [var timings: CMSampleBuffer.TimingPerSample?](cmsamplebuffer/samplepropertiescollection/timings.md)
  Access sample timings.
### Subscripts
- [subscript(Int) -> CMSampleBuffer.SampleProperties](cmsamplebuffer/samplepropertiescollection/subscript(_:).md)
  Accesses the element at the specified position.

## Relationships

### Conforms To
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [RandomAccessCollection](../Swift/RandomAccessCollection.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [Sequence](../Swift/Sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/samplepropertiescollection)*