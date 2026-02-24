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

- `desc`: A [`CMFormatDescription`](https://developer.apple.com/documentation/CoreMedia/CMFormatDescription) that defines the metadata to be supplied by the client. Throws [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) if `NULL` is passed.
- `clock`: A [`CMClock`](https://developer.apple.com/documentation/CoreMedia/CMClock) that provides the timebase for the supplied samples. Throws [`invalidArgumentException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/invalidArgumentException) if `NULL` is passed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturemetadatainput/init(formatdescription:clock:))*