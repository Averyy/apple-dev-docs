# CSSM_DL_DbCreate

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_DL_DbCreate(CSSM_DL_HANDLE DLHandle, const char *DbName, const CSSM_NET_ADDRESS *DbLocation, const CSSM_DBINFO *DBInfo, CSSM_DB_ACCESS_TYPE AccessRequest, const CSSM_RESOURCE_CONTROL_CONTEXT *CredAndAclEntry, const void *OpenParameters, CSSM_DB_HANDLE *DbHandle);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_dl_dbcreate)*