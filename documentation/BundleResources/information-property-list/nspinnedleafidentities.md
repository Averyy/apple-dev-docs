# NSPinnedLeafIdentities

**Framework**: Bundle Resources  
**Kind**: dictionary

A list of allowed leaf certificates for a given domain name.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- visionOS 1.0+

#### Discussion

Provide an array of dictionaries as the value for this key. Each dictionary in the array contains the [`SPKI-SHA256-BASE64`](information-property-list/nspinnedleafidentities/spki-sha256-base64.md) key with a value that represents the Base64-encoded SHA-256 digest of an X.509 certificate’s DER-encoded ASN.1 Subject Public Key Info (SPKI) structure.

```console
NSPinnedLeafIdentities : Array {
    Dictionary {
        SPKI-SHA256-BASE64 : String
    }
}
```

When making a network connection to a named domain, App Transport Security (ATS) blocks the connection unless it can find the SPKI digest of the leaf certificate presented by the server among the digests in this array. Consider including more than one leaf certificate to allow for server-side configuration changes.

You must include this key or the [`NSPinnedCAIdentities`](information-property-list/nspinnedcaidentities.md) key or both in each domain-specific [`NSPinnedDomains`](information-property-list/nsapptransportsecurity/nspinneddomains.md) subdictionary. If you include both, then both must produce a match.

## Topics

### Key Digests
- [SPKI-SHA256-BASE64](information-property-list/nspinnedleafidentities/spki-sha256-base64.md)
  The digest of an X.509 certificate’s Subject Public Key Info structure.

## See Also

- [NSPinnedCAIdentities](information-property-list/nspinnedcaidentities.md)
  A list of allowed Certificate Authority certificates for a given domain name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nspinnedleafidentities)*