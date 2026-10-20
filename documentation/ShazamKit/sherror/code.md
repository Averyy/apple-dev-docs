# SHError.Code

**Framework**: ShazamKit  
**Kind**: enum  
**Role**: Enumeration

Codes for the errors that Shazam produces.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum Code
```

```c
enum SHErrorCode : NSInteger;
```

## Topics

### Matching errors
- [SHError.Code.matchAttemptFailed](./code/matchattemptfailed.md)
  The error code to indicate when a Shazam Music catalog server issue prevents finding a match.
### Signature errors
- [SHError.Code.signatureInvalid](./code/signatureinvalid.md)
  The error code to indicate that the system is unable to generate a signature from the audio.
- [SHError.Code.signatureDurationInvalid](./code/signaturedurationinvalid.md)
  The error code to indicate that the length of the generated signature is too long or too short to make a match in the catalog.
### Audio format errors
- [SHError.Code.invalidAudioFormat](./code/invalidaudioformat.md)
  The error code to indicate an unsupported audio format.
- [SHError.Code.audioDiscontinuity](./code/audiodiscontinuity.md)
  The error code to indicate the use of noncontiguous audio to request a match.
### Catalog errors
- [SHError.Code.customCatalogInvalidURL](./code/customcataloginvalidurl.md)
  The error code to indicate that the format for the custom catalog URL is invalid.
- [SHError.Code.customCatalogInvalid](./code/customcataloginvalid.md)
  The error code to indicate when the custom catalog fails to load due to an invalid format.
### Library sync errors
- [SHError.Code.mediaItemFetchFailed](./code/mediaitemfetchfailed.md)
  The error code to indicate when the system fails to fetch one or more media items.
- [SHError.Code.mediaLibrarySyncFailed](./code/medialibrarysyncfailed.md)
  The error code to indicate when the system fails to add one or more media items to the user’s Shazam library.
### Framework errors
- [SHError.Code.internalError](./code/internalerror.md)
  The error code to indicate a generic framework error.
### Querying the error domain
- [let SHErrorDomain: String](../sherrordomain.md)
  The error domain for specific errors for ShazamKit.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting an error
- [Error Constants](../error-constants.md)
  Error code constants for framework operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/sherror/code)*