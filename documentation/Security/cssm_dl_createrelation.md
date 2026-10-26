# CSSM_DL_CreateRelation

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_DL_CreateRelation(CSSM_DL_DB_HANDLE DLDBHandle, CSSM_DB_RECORDTYPE RelationID, const char *RelationName, uint32 NumberOfAttributes, const CSSM_DB_SCHEMA_ATTRIBUTE_INFO *pAttributeInfo, uint32 NumberOfIndexes, const CSSM_DB_SCHEMA_INDEX_INFO *pIndexInfo);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_dl_createrelation)*