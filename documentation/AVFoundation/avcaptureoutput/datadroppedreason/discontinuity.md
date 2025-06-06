# AVCaptureOutput.DataDroppedReason.discontinuity

**Framework**: AVFoundation  
**Kind**: case

The system dropped data because the device providing data experienced a discontinuity, and the output lost an unknown number of data objects.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
case discontinuity
```

#### Discussion

A discontinuity is a situation where the capture system can’t ensure that minimal time passes between the capture of data buffers. This kind of situation can arise when the system as a whole is too busy to handle the data.

## See Also

- [AVCaptureOutput.DataDroppedReason.none](avcaptureoutput/datadroppedreason/none.md)
  The system didn’t drop data.
- [AVCaptureOutput.DataDroppedReason.lateData](avcaptureoutput/datadroppedreason/latedata.md)
  The system dropped data because you’ve configured capture output to drop data when delegate queue is in a blocked state, and there’s data to deliver.
- [AVCaptureOutput.DataDroppedReason.outOfBuffers](avcaptureoutput/datadroppedreason/outofbuffers.md)
  The system dropped data because the capture output exhausted its internal pool of memory buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureoutput/datadroppedreason/discontinuity)*