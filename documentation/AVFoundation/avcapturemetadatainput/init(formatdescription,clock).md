# init(formatDescription:clock:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates capture metadata input to provide timed groups to a capture session.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
init(formatDescription desc: CMMetadataFormatDescription, clock: CMClock)
```

```objc
- (instancetype) initWithFormatDescription:(CMMetadataFormatDescriptionRef) desc clock:(CMClockRef) clock;
```

## Parameters

- `desc`: A [`CMFormatDescription`](../../CoreMedia/cmformatdescription.md) that defines the metadata to be supplied by the client. Throws [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) if `NULL` is passed.
- `clock`: A [`CMClock`](../../CoreMedia/cmclock.md) that provides the timebase for the supplied samples. Throws [`invalidArgumentException`](../../Foundation/nsexceptionname/invalidargumentexception.md) if `NULL` is passed.

## See Also

### Creating metadata input
- [+ metadataInputWithFormatDescription:clock:](./metadatainputwithformatdescription_clock_.md)
  Returns a metadata input instance that allows clients to provide timed metadata groups to a capture session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput/init(formatdescription:clock:))*