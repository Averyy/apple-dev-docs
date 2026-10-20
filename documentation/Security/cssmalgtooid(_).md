# cssmAlgToOid(_:)

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+

## Declaration

```swift
func cssmAlgToOid(_ algId: CSSM_ALGORITHMS) -> UnsafePointer<SecAsn1Oid>!
```

```c
const SecAsn1Oid *cssmAlgToOid(CSSM_ALGORITHMS algId);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssmalgtooid(_:))*