# init(from:)

**Framework**: Apple Archive  
**Kind**: init

Returns a new encryption context from the specified encrypted stream.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
init?(from stream: ArchiveByteStream)
```

#### Discussion

Use this function to either reopen an encrypted stream for writing or open an encrypted stream for reading. After you open the encryption context, query the archive properties and insert the credentials necessary to unlock and sign the stream.

In the case of a signed stream, if you’ve set a private signing key with [`AEAContextSetSigningPrivateKey`](aeacontextsetsigningprivatekey.md) the context signs the stream on close.

If you haven’t set a private key, the context still requires a public key, as it’s tied to the stream. After you close the encryption stream, you can pass the private signing key to the context by calling the stream-signing function [`AEAStreamSign`](aeastreamsign.md).

## Parameters

- `stream`: The encrypted stream that provides the profile, signature mode, encryption mode, and authorization data.

## See Also

- [init(profile: ArchiveEncryptionContext.Profile, compressionAlgorithm: ArchiveCompression, compressionBlockSize: Int)](archiveencryptioncontext/init(profile:compressionalgorithm:compressionblocksize:).md)
  Returns a new encryption context from the specified profile, compression algorithm, and block size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applearchive/archiveencryptioncontext/init(from:))*