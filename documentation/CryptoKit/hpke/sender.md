# HPKE.Sender

**Framework**: Apple CryptoKit  
**Kind**: struct  
**Role**: Structure

A type that represents the sending side of an HPKE message exchange.

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
struct Sender
```

#### Overview

To create encrypted messages, initialize a `Sender` specifying the appropriate cipher suite, the recipient’s public key, and the additional cryptographic material relevant to your chosen mode of operation. Call [`seal(_:)`](./sender/seal%28_%29.md) or [`seal(_:authenticating:)`](./sender/seal%28_,authenticating%29.md) on the `Sender` instance for each message in turn to retrieve its ciphertext. The recipient of the messages needs to process them in the same order as the `Sender`, using the same encryption mode, cipher suite, and key schedule information (`info`), as well as the `Sender`’s [`encapsulatedKey`](./sender/encapsulatedkey.md).

## Topics

### Initializers
- [init<PK>(recipientKey: PK, ciphersuite: HPKE.Ciphersuite, info: Data) throws](./sender/init%28recipientkey,ciphersuite,info%29-56p88.md)
  Creates a sender in base mode.
- [init<PK>(recipientKey: PK, ciphersuite: HPKE.Ciphersuite, info: Data) throws](./sender/init%28recipientkey,ciphersuite,info%29-swk5.md)
  Creates a sender in base mode.
- [init<SK>(recipientKey: SK.PublicKey, ciphersuite: HPKE.Ciphersuite, info: Data, authenticatedBy: SK) throws](./sender/init%28recipientkey,ciphersuite,info,authenticatedby%29.md)
  Creates a sender in authentication mode.
- [init<SK>(recipientKey: SK.PublicKey, ciphersuite: HPKE.Ciphersuite, info: Data, authenticatedBy: SK, presharedKey: SymmetricKey, presharedKeyIdentifier: Data) throws](./sender/init%28recipientkey,ciphersuite,info,authenticatedby,presharedkey,presharedkeyidentifier%29.md)
  Creates a sender in authentication and preshared key mode.
- [init<PK>(recipientKey: PK, ciphersuite: HPKE.Ciphersuite, info: Data, presharedKey: SymmetricKey, presharedKeyIdentifier: Data) throws](./sender/init%28recipientkey,ciphersuite,info,presharedkey,presharedkeyidentifier%29.md)
  Creates a sender in preshared key (PSK) mode.
### Instance Properties
- [let encapsulatedKey: Data](./sender/encapsulatedkey.md)
  The encapsulated symmetric key that the recipient uses to decrypt messages.
### Instance Methods
- [func exportSecret<Context>(context: Context, outputByteCount: Int) throws -> SymmetricKey](./sender/exportsecret%28context,outputbytecount%29.md)
  Exports a secret given domain-separation context and the desired output length.
- [func seal<M>(M) throws -> Data](./sender/seal%28_%29.md)
  Encrypts the given cleartext message.
- [func seal<M, AD>(M, authenticating: AD) throws -> Data](./sender/seal%28_,authenticating%29.md)
  Encrypts the given cleartext message and attaches additional authenticated data.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Sending and receiving messages
- [struct Recipient](./recipient.md)
  A type that represents the receiving side of an HPKE message exchange.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/hpke/sender)*