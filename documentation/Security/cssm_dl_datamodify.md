# CSSM_DL_DataModify

**Framework**: Security  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.0+ - Deprecated in 10.7

## Declaration

```c
CSSM_RETURN CSSM_DL_DataModify(CSSM_DL_DB_HANDLE DLDBHandle, CSSM_DB_RECORDTYPE RecordType, CSSM_DB_UNIQUE_RECORD_PTR UniqueRecordIdentifier, const CSSM_DB_RECORD_ATTRIBUTE_DATA *AttributesToBeModified, const SecAsn1Item *DataToBeModified, CSSM_DB_MODIFY_MODE ModifyMode);
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cssm_dl_datamodify)*