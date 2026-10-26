# SecKeychainItemGetUniqueRecordID

**Framework**: Security  
**Kind**: func  
**Role**: Function

Returns a CSSM unique record for the given keychain item object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

> **Deprecated**: The common security services manager module is no longer used.

## Declaration

```c
OSStatus SecKeychainItemGetUniqueRecordID(SecKeychainItemRef itemRef, const CSSM_DB_UNIQUE_RECORD **uniqueRecordID);
```

#### Return Value

A result code. See [Security Framework Result Codes](./security-framework-result-codes.md).

#### Discussion

> ❗ **Important**:  This function is deprecated. The common security services manager module is no longer used.

## Parameters

- `itemRef`: A keychain item object.
- `uniqueRecordID`: On return, a pointer to a CSSM unique record for the given item. The unique record is valid until the item object is released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/seckeychainitemgetuniquerecordid)*