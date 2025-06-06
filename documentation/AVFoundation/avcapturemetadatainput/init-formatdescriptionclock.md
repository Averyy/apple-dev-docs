# init(formatDescription:clock:)

**Framework**: AVFoundation  
**Kind**: init

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

## Parameters

- `desc`: A   that defines the metadata to be supplied by the client. Throws   if   is passed.
- `clock`: A  doc://com.apple.documentation/documentation/coremedia/cmclock-u5q  that provides the timebase for the supplied samples. Throws   if   is passed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput/init(formatdescription:clock:))*