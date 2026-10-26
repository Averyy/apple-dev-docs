# CSSM_DL_DbOpen

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_DL_DbOpen(CSSM_DL_HANDLE DLHandle, const char *DbName, const CSSM_NET_ADDRESS *DbLocation, CSSM_DB_ACCESS_TYPE AccessRequest, const CSSM_ACCESS_CREDENTIALS *AccessCred, const void *OpenParameters, CSSM_DB_HANDLE *DbHandle);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_dl_dbopen)*