# SPKI-SHA256-BASE64

**Framework**: Bundle Resources  
**Kind**: typealias

The digest of an X.509 certificate’s Subject Public Key Info structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- visionOS 1.0+

#### Discussion

You represent a pinned certificate using the Base64-encoded SHA-256 digest of an X.509 certificate’s DER-encoded ASN.1 Subject Public Key Info (SPKI) structure. For a PEM-encoded public-key certificate stored in the file `ca.pem`, you can calculate the [`SPKI-SHA256-BASE64`](information-property-list/nspinnedcaidentities/spki-sha256-base64.md) value with the following `openssl` commands:

```sh
% cat ca.pem |
      openssl x509 -inform pem -noout -outform pem -pubkey |
      openssl pkey -pubin -inform pem -outform der |
      openssl dgst -sha256 -binary |
      openssl enc -base64
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nspinnedcaidentities/spki-sha256-base64)*