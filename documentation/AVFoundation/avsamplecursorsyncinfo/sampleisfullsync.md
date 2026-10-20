# sampleIsFullSync

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether a sample is a full sync sample.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var sampleIsFullSync: ObjCBool
```

```c
BOOL sampleIsFullSync;
```

#### Discussion

A full sync sample, also called a Instantaneous Decoder Refresh sample, is sufficient in itself to completely resynchronize a decoder.

## See Also

### Sync information
- [var sampleIsPartialSync: ObjCBool](./sampleispartialsync.md)
  A Boolean value that indicates whether a sample is a partial sync sample.
- [var sampleIsDroppable: ObjCBool](./sampleisdroppable.md)
  A Boolean value that indicates whether a sample is droppable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplecursorsyncinfo/sampleisfullsync)*