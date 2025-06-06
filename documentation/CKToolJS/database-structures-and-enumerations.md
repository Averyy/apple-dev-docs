# Database Structures and Enumerations

**Framework**: CKTool JS

## Topics

### Structures
- [CKDBAsset](ckdbasset.md)
  An object that represents an asset uploaded to CloudKit.
- [CKDBAssetUploadUrlResponse](ckdbassetuploadurlresponse.md)
  An object that represents the results of creating an asset upload URL.
- [CKDBChangeMetadata](ckdbchangemetadata.md)
  An object that represents metadata about a record change via creation or modification.
- [CKDBCreateAssetUploadUrlRequestBody](ckdbcreateassetuploadurlrequestbody.md)
  An object that represents the request for creating an asset upload URL.
- [CKDBCreateRecordRequestBody](ckdbcreaterecordrequestbody.md)
  An object that represents the request to create a new record.
- [CKDBCreateZoneRequestBody](ckdbcreatezonerequestbody.md)
  An object that represents the request to create a new zone.
- [CKDBDeleteRecordsByQueryRequestBody](ckdbdeleterecordsbyqueryrequestbody.md)
  An object that represents the request to delete multiple records that match a query.
- [CKDBDeletedRecordResult](ckdbdeletedrecordresult.md)
  An object that represents a deleted record result.
- [CKDBErrorRecordResult](ckdberrorrecordresult.md)
  An object that represents a record lookup failure.
- [CKDBExistingRecordResult](ckdbexistingrecordresult.md)
  An object that represents a successful record result.
- [CKDBForRecord](ckdbforrecord.md)
  An object that represents a record that is being shared.
- [CKDBLocation](ckdblocation.md)
  An object that represents a location field value.
- [CKDBLookupRecordsRequestBody](ckdblookuprecordsrequestbody.md)
  An object that represents the request for looking up multiple records by record name.
- [CKDBLookupRecordsResponse](ckdblookuprecordsresponse.md)
  An object that represents the results of a batch record lookup operation.
- [CKDBModifyRecordRequestBody](ckdbmodifyrecordrequestbody.md)
  An object that represents the request for updating an existing record.
- [CKDBNullableReference](ckdbnullablereference.md)
  An object that represents a reference to another record.
- [CKDBPagedBatchDeleteResponse](ckdbpagedbatchdeleteresponse.md)
  An object that represents the results of a paginated batch delete operation.
- [CKDBQuery](ckdbquery.md)
  An object that represents a query for searching records.
- [CKDBQueryFilter](ckdbqueryfilter.md)
  An object that represents the logical conditions for determining whether a record matches the query.
- [CKDBQueryRecordsRequestBody](ckdbqueryrecordsrequestbody.md)
  An object that represents the request for fetching multiple records that match a query.
- [CKDBQuerySort](ckdbquerysort.md)
  An object that represents a sort descriptor that specifies how to order fetched records.
- [CKDBRecord](ckdbrecord.md)
  An object that represents a record in a database.
- [CKDBRecordChangesRequestBody](ckdbrecordchangesrequestbody.md)
  An object that represents the request for fetching changes since a specified zone change token.
- [CKDBRecordChangesResponse](ckdbrecordchangesresponse.md)
  An object that represents the results of a record changes lookup operation.
- [CKDBRecordReference](ckdbrecordreference.md)
  An object that represents a reference to a CloudKit database record.
- [CKDBRecordResponse](ckdbrecordresponse.md)
  An object that represents the results of a record lookup operation.
- [CKDBRecordResult](ckdbrecordresult.md)
  An object that represents a record when the lookup operation can potentially return deleted records or fail partially when looking up some of the record.
- [CKDBRecordsResponse](ckdbrecordsresponse.md)
  An object that represents the results of a batch record lookup operation.
- [CKDBResolveRecordRequestBody](ckdbresolverecordrequestbody.md)
  An object that represents a request for fetching a record given its `shortGuid`.
- [CKDBResolveRecordResponse](ckdbresolverecordresponse.md)
  An object that represents the results of looking up a record by its `shortGuid`.
- [CKDBResolvedRecord](ckdbresolvedrecord.md)
  An object that represents a shared record fetched using its `shortGuid`.
- [CKDBSchemaImportRequestBody](ckdbschemaimportrequestbody.md)
  An object that contains a schema file to be applied to a container environment.
- [CKDBSessionUser](ckdbsessionuser.md)
  An object that represents the current user.
- [CKDBSessionUserResponse](ckdbsessionuserresponse.md)
  An object that contains the result of looking up the current user.
- [CKDBShareParticipant](ckdbshareparticipant.md)
  An object that represents a share participant.
- [CKDBSharePotentialParticipant](ckdbsharepotentialparticipant.md)
  An object that represents a potential participant for a share.
- [CKDBStableUrl](ckdbstableurl.md)
  Internal use only.
- [CKDBStreamingAsset](ckdbstreamingasset.md)
  A streaming asset object that represents a streaming asset in CloudKit.
- [CKDBUserIdentity](ckdbuseridentity.md)
  An object that identifies a user participating in a share.
- [CKDBUserIdentityLookupInfo](ckdbuseridentitylookupinfo.md)
  An object that represents lookup information for a user.
- [CKDBUserNameComponents](ckdbusernamecomponents.md)
  An object that represents the user’s name.
- [CKDBValidateSchemaResponse](ckdbvalidateschemaresponse.md)
  The response object after validating the uploaded schema string.
- [CKDBZone](ckdbzone.md)
  An object that represents a CloudKit database zone.
- [CKDBZoneId](ckdbzoneid.md)
  An object that represents a CloudKit database zone identifier.
- [CKDBZoneResponse](ckdbzoneresponse.md)
  An object that represents results of fetching a zone.
- [CKDBZonesResponse](ckdbzonesresponse.md)
  An object that represents results of fetching multiple zones.
### Enumerations
- [CKDBPermissionType](ckdbpermissiontype.md)
  The participant’s read and write permissions.
- [CKDBQueryFilterType](ckdbqueryfiltertype.md)
  An object that represents the type of a filter that indicates the comparison operator when applying the filter.
- [CKDBQuerySortOrder](ckdbquerysortorder.md)
  An enumeration that represents the order to use when sorting records.
- [CKDBRecordReferenceAction](ckdbrecordreferenceaction.md)
  An object that represents the action to be performed for the referenced record.
- [CKDBShareAcceptanceStatus](ckdbshareacceptancestatus.md)
  An enumeration that indicates the status of accepting the shared record.
- [CKDBShareParticipantType](ckdbshareparticipanttype.md)
  An enumeration that represents the type of a share participant.

## See Also

- [Field Values](field-values.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/database-structures-and-enumerations)*