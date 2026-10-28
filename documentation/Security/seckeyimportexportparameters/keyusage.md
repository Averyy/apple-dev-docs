# keyUsage

**Framework**: Security  
**Kind**: property  
**Role**: Instance Property

A word of bits constituting the low-level use flags for imported keys.

**Availability**:
- macOS 10.0+

## Declaration

```swift
var keyUsage: CSSM_KEYUSE
```

```c
CSSM_KEYUSE keyUsage;
```

## Discussion

Use flags defined in `cssmtype.h`. If this field is `0` or `keyParams` is `NULL`, the default value is `CSSM_KEYUSE_ANY`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeyimportexportparameters/keyusage)*