# cssmOidToAlg(_:_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```swift
func cssmOidToAlg(_ oid: UnsafePointer<SecAsn1Oid>!, _ alg: UnsafeMutablePointer<CSSM_ALGORITHMS>!) -> Bool
```

```c
bool cssmOidToAlg(const SecAsn1Oid *oid, CSSM_ALGORITHMS *alg);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssmoidtoalg(_:_:))*