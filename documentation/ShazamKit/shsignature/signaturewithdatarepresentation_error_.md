# signatureWithDataRepresentation:error:

**Framework**: ShazamKit  
**Kind**: method  
**Role**: Type Method

Creates a signature object from raw data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```objc
+ (SHSignature *) signatureWithDataRepresentation:(NSData *) dataRepresentation error:(NSError **) error;
```

#### Return Value

A signature if the raw data is a valid signature; otherwise, `nil`.

## Parameters

- `dataRepresentation`: The raw data for the signature.
- `error`: The error that occurs; otherwise, `nil`.

## See Also

### Creating a signature object
- [init(dataRepresentation: Data) throws](./init%28datarepresentation%29.md)
  Creates a signature object from raw data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shazamkit/shsignature/signaturewithdatarepresentation:error:)*