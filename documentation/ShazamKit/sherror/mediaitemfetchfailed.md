# mediaItemFetchFailed

**Framework**: ShazamKit  
**Kind**: property  
**Role**: Type Property

The error code to indicate when the system fails to fetch one or more media items.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static var mediaItemFetchFailed: SHError.Code { get }
```

## See Also

### Constants
- [static var matchAttemptFailed: SHError.Code](./matchattemptfailed.md)
  The error code to indicate when a Shazam Music catalog server issue prevents finding a match.
- [static var signatureInvalid: SHError.Code](./signatureinvalid.md)
  The error code to indicate that the system is unable to generate a signature from the audio.
- [static var signatureDurationInvalid: SHError.Code](./signaturedurationinvalid.md)
  The error code to indicate that the length of the generated signature is too long or too short to make a match in the catalog.
- [static var invalidAudioFormat: SHError.Code](./invalidaudioformat.md)
  The error code to indicate an unsupported audio format.
- [static var internalError: SHError.Code](./internalerror.md)
  The error code to indicate a generic framework error.
- [static var audioDiscontinuity: SHError.Code](./audiodiscontinuity.md)
  The error code to indicate the use of noncontiguous audio to request a match.
- [static var customCatalogInvalidURL: SHError.Code](./customcataloginvalidurl.md)
  The error code to indicate that the format for the custom catalog URL is invalid.
- [static var customCatalogInvalid: SHError.Code](./customcataloginvalid.md)
  The error code to indicate when the custom catalog fails to load due to an invalid format.
- [static var mediaLibrarySyncFailed: SHError.Code](./medialibrarysyncfailed.md)
  The error code that indicates when the system fails to add media items to or remove items from the user’s Shazam library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/sherror/mediaitemfetchfailed)*