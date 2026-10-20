# FormatFlagIsNonInterleaved

**Framework**: AudioDriverKit  
**Kind**: case

A flag to indicate whether the channels interleave their samples in the data.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
FormatFlagIsNonInterleaved
```

#### Discussion

Set this flag if the each channel lays out its samples contiguously, with the channels layed out end to end. Clear this flag if each frame lays out its samples contiguously, with the frames layed out end to end.

## See Also

- [LinearPCMFormatFlagIsNonInterleaved](audiodriverkit/iouseraudioformatflags/linearpcmformatflagisnoninterleaved.md)
  A flag to indicate whether PCM channels interleave their samples in the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudioformatflags/formatflagisnoninterleaved)*