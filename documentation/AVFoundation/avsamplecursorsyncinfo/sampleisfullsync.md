# sampleIsFullSync

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether a sample is a full sync sample.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var sampleIsFullSync: ObjCBool
```

#### Discussion

A full sync sample, also called a Instantaneous Decoder Refresh sample, is sufficient in itself to completely resynchronize a decoder.

## See Also

- [var sampleIsPartialSync: ObjCBool](avsamplecursorsyncinfo/sampleispartialsync.md)
  A Boolean value that indicates whether a sample is a partial sync sample.
- [var sampleIsDroppable: ObjCBool](avsamplecursorsyncinfo/sampleisdroppable.md)
  A Boolean value that indicates whether a sample is droppable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursorsyncinfo/sampleisfullsync)*