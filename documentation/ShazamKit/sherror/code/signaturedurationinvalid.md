# SHError.Code.signatureDurationInvalid

**Framework**: ShazamKit  
**Kind**: case

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
case signatureDurationInvalid
```

#### Discussion

This error occurs when the length of the generated signature is less than [`minimumQuerySignatureDuration`](shcatalog/minimumquerysignatureduration.md) or greater than [`maximumQuerySignatureDuration`](shcatalog/maximumquerysignatureduration.md) for the session [`catalog`](shsession/catalog.md).

## See Also

- [SHError.Code.signatureInvalid](sherror/code/signatureinvalid.md)
  The error code to indicate that the system is unable to generate a signature from the audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/sherror/code/signaturedurationinvalid)*