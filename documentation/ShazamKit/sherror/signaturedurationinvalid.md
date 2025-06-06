# signatureDurationInvalid

**Framework**: ShazamKit  
**Kind**: property

The error code to indicate that the length of the generated signature is too long or too short to make a match in the catalog.

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
static var signatureDurationInvalid: SHError.Code { get }
```

#### Discussion

This error occurs when the length of the generated signature is less than [`minimumQuerySignatureDuration`](shcatalog/minimumquerysignatureduration.md) or greater than [`maximumQuerySignatureDuration`](shcatalog/maximumquerysignatureduration.md) for the session [`catalog`](shsession/catalog.md).

## See Also

- [static var matchAttemptFailed: SHError.Code](sherror/matchattemptfailed.md)
  The error code to indicate when a Shazam Music catalog server issue prevents finding a match.
- [static var signatureInvalid: SHError.Code](sherror/signatureinvalid.md)
  The error code to indicate that the system is unable to generate a signature from the audio.
- [static var invalidAudioFormat: SHError.Code](sherror/invalidaudioformat.md)
  The error code to indicate an unsupported audio format.
- [static var internalError: SHError.Code](sherror/internalerror.md)
  The error code to indicate a generic framework error.
- [static var audioDiscontinuity: SHError.Code](sherror/audiodiscontinuity.md)
  The error code to indicate the use of noncontiguous audio to request a match.
- [static var customCatalogInvalidURL: SHError.Code](sherror/customcataloginvalidurl.md)
  The error code to indicate that the format for the custom catalog URL is invalid.
- [static var customCatalogInvalid: SHError.Code](sherror/customcataloginvalid.md)
  The error code to indicate when the custom catalog fails to load due to an invalid format.
- [static var mediaItemFetchFailed: SHError.Code](sherror/mediaitemfetchfailed.md)
  The error code to indicate when the system fails to fetch one or more media items.
- [static var mediaLibrarySyncFailed: SHError.Code](sherror/medialibrarysyncfailed.md)
  The error code that indicates when the system fails to add media items to or remove items from the user’s Shazam library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/sherror/signaturedurationinvalid)*