# SecExternalItemType.itemTypeAggregate

**Framework**: Security  
**Kind**: case  
**Role**: Case

Indicates a set of certificates or certificates and private keys.

**Availability**:
- macOS 10.0+

## Declaration

```swift
case itemTypeAggregate
```

```c
kSecItemTypeAggregate
```

## Discussion

Possible values include [`SecExternalFormat.formatPKCS7`](../secexternalformat/formatpkcs7.md), [`SecExternalFormat.formatPKCS12`](../secexternalformat/formatpkcs12.md), or [`SecExternalFormat.formatPEMSequence`](../secexternalformat/formatpemsequence.md) formats (see [`SecExternalFormat`](../secexternalformat.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secexternalitemtype/itemtypeaggregate)*