# init(certificate:objectID:)

**Framework**: CryptoTokenKit  
**Kind**: init

Initializes a token keychain certificate with data from the specified certificate reference and a given object ID.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
init?(certificate certificateRef: SecCertificate, objectID: TKToken.ObjectID)
```

#### Return Value

A new token keychain certificate.

#### Discussion

This is the designated initializer.

## Parameters

- `certificateRef`: You can create a   value from a data object using the   function.
- `objectID`: The object ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenkeychaincertificate/init(certificate:objectid:))*