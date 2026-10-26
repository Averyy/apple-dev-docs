# SecKeyGetCSSMKey

**Framework**: Security  
**Kind**: func  
**Role**: Function

Retrieves a pointer to the `CSSM_KEY` structure containing the key stored in a keychain item.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
OSStatus SecKeyGetCSSMKey(SecKeyRef key, const CSSM_KEY **cssmKey);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

The `CSSM_KEY` structure is used to represent keys in CSSM and is used as an input value to several CSSM functions. The `CSSM_KEY` structure is valid until the keychain item object is released.

## Parameters

- `key`: A keychain key item object.
- `cssmKey`: A pointer to a `CSSM_KEY` structure for the specified key. You should not modify or free this data, because it is owned by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeygetcssmkey)*