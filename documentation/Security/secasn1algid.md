# SecAsn1AlgId

**Framework**: Security  
**Kind**: struct  
**Role**: Structure

A structure identifying an ASN.1 algorithm by its OID, and its corresponding parameters.

**Availability**:
- macOS 10.0+ - Deprecated in 12.0

> **Deprecated**: SecAsn1 is not supported

## Declaration

```swift
struct SecAsn1AlgId
```

```c
typedef struct { ... } SecAsn1AlgId;
```

## Topics

### Algorithm Characteristics
- [var algorithm: SecAsn1Oid](./secasn1algid/algorithm.md)
- [var parameters: SecAsn1Item](./secasn1algid/parameters.md)
### Creating a Structure
- [init()](./secasn1algid/init%28%29.md)
- [init(algorithm: SecAsn1Oid, parameters: SecAsn1Item)](./secasn1algid/init%28algorithm,parameters%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/secasn1algid)*