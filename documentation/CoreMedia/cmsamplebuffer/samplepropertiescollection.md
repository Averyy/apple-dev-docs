# CMSampleBuffer.SamplePropertiesCollection

**Framework**: Core Media  
**Kind**: struct  
**Role**: Structure

Fixed size collection of sample information.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct SamplePropertiesCollection
```

## Overview

This collection contains one element for each sample in the sample buffer. The size of collection is fixed to the number of samples in a sample buffer. Convenience static methods are available on timings & sizes to create this collection by specifying just one value.

## Topics

### Initializers
- [init()](./samplepropertiescollection/init%28%29.md)
  Creates an empty collection.
- [init(some Collection<CMSampleBuffer.SampleProperties>)](./samplepropertiescollection/init%28_%29.md)
- [init(sampleCount: Int, sizes: CMSampleBuffer.SizePerSample?, timings: CMSampleBuffer.TimingPerSample?, attachments: [CMSampleBuffer.SampleAttachments]?)](./samplepropertiescollection/init%28samplecount,sizes,timings,attachments%29.md)
  Create a collection with specified sample information.
### Instance Properties
- [var attachments: [CMSampleBuffer.SampleAttachments]?](./samplepropertiescollection/attachments.md)
  Access sample attachments.
- [var count: Int](./samplepropertiescollection/count.md)
  The number of elements in the collection.
- [var endIndex: Int](./samplepropertiescollection/endindex.md)
  The position one greater than the last valid subscript argument.
- [var sizes: CMSampleBuffer.SizePerSample?](./samplepropertiescollection/sizes.md)
  Access sample sizes.
- [var startIndex: Int](./samplepropertiescollection/startindex.md)
  The position of the first element.
- [var timings: CMSampleBuffer.TimingPerSample?](./samplepropertiescollection/timings.md)
  Access sample timings.
### Subscripts
- [subscript(Int) -> CMSampleBuffer.SampleProperties](./samplepropertiescollection/subscript%28_%29.md)
  Accesses the element at the specified position.

## Relationships

### Conforms To
- [BidirectionalCollection](../../Swift/bidirectionalcollection.md)
- [Collection](../../Swift/collection.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [MutableCollection](../../Swift/mutablecollection.md)
- [RandomAccessCollection](../../Swift/randomaccesscollection.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [Sequence](../../Swift/sequence.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremedia/cmsamplebuffer/samplepropertiescollection)*