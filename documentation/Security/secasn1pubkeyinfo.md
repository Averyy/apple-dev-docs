# SecAsn1PubKeyInfo

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

A structure containing a public key and its associated algorithm.

**Availability**:
- macOS 10.0+ - Deprecated in 12.0

> **Deprecated**: SecAsn1 is not supported

## Declaration

```swift
struct SecAsn1PubKeyInfo
```

```c
typedef struct { ... } SecAsn1PubKeyInfo;
```

## Topics

### Public Key Characteristics
- [var subjectPublicKey: SecAsn1Item](./secasn1pubkeyinfo/subjectpublickey.md)
- [var algorithm: SecAsn1AlgId](./secasn1pubkeyinfo/algorithm.md)
### Creating a Public Key
- [init()](./secasn1pubkeyinfo/init%28%29.md)
- [init(algorithm: SecAsn1AlgId, subjectPublicKey: SecAsn1Item)](./secasn1pubkeyinfo/init%28algorithm,subjectpublickey%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secasn1pubkeyinfo)*