# SHError.Code.signatureInvalid

**Framework**: ShazamKit  
**Kind**: case

The error code to indicate that the system is unable to generate a signature from the audio.

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
case signatureInvalid
```

#### Discussion

The most common cause of this error is silent audio input.

## See Also

- [SHError.Code.signatureDurationInvalid](sherror/code/signaturedurationinvalid.md)
  The error code to indicate that the length of the generated signature is too long or too short to make a match in the catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/sherror/code/signatureinvalid)*