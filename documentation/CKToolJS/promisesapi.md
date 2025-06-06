# PromisesApi

**Framework**: CKTool JS  
**Kind**: class

A class that exposes promise-based functions for interacting with the API.

**Availability**:
- CKTool JS 1.2.15+

## Declaration

```swift
interface PromisesApi
```

## Mentions

- [Integrating CloudKit access into your JavaScript automation scripts](integrating-cloudkit-access-into-your-javascript-automation-scripts.md)

#### Overview

You use an instance of `PromisesApi` to interact with the API. Methods on this class return promises that complete with a response object.

## Topics

### Record Management
- [acceptRecord](promisesapi/acceptrecord.md)
  Accepts a share on behalf of the current user.
- [createRecord](promisesapi/createrecord.md)
  Creates a new record.
- [deleteRecord](promisesapi/deleterecord.md)
  Deletes a single record.
- [deleteRecordsByQuery](promisesapi/deleterecordsbyquery.md)
  Deletes records matching the provided query.
- [getRecord](promisesapi/getrecord.md)
  Returns a record’s details.
- [lookupRecords](promisesapi/lookuprecords.md)
  Fetches multiple records by record name.
- [queryRecordChanges](promisesapi/queryrecordchanges.md)
  Returns records that changed since a specified sync token or since a zone was created.
- [queryRecords](promisesapi/queryrecords.md)
  Returns a collection of records matching the provided query.
- [resolveRecord](promisesapi/resolverecord.md)
  Fetches information about records given their shortGuid properties.
- [updateRecord](promisesapi/updaterecord.md)
  Updates an existing record.
### Zone Management
- [createZone](promisesapi/createzone.md)
  Creates a new zone.
- [deleteZone](promisesapi/deletezone.md)
  Deletes a zone.
- [getZone](promisesapi/getzone.md)
  Returns details for a zone.
- [getZones](promisesapi/getzones.md)
  Returns a collection of zones.
### Database Management
- [exportSchema](promisesapi/exportschema.md)
  Downloads the container’s schema.
- [getContainers](promisesapi/getcontainers.md)
  Fetches containers for a team.
- [importSchema](promisesapi/importschema.md)
  Uploads a file that defines the new schema for the container.
- [resetConfigToProduction](promisesapi/resetconfigtoproduction.md)
  Resets the container configuration to production.
- [resetToProduction](promisesapi/resettoproduction.md)
  Resets the schema of the environment to production.
- [validateSchema](promisesapi/validateschema.md)
  Validates the uploaded schema file for the container.
### Database Field Values, Structures and Enumerations
- [Field Values](field-values.md)
- [Database Structures and Enumerations](database-structures-and-enumerations.md)
### Asset Creation
- [createAssetUploadUrl](promisesapi/createassetuploadurl.md)
  Creates a new URL for uploading assets.
### User and Team
- [getSessionUser](promisesapi/getsessionuser.md)
  Returns details for the user in current session.
- [getTeams](promisesapi/getteams.md)
  Fetches a list of teams the current user is in.
- [Team](team.md)
  Details of a developer team.
- [TeamsResponse](teamsresponse.md)
  Response object for a list of teams.
### Initialization
- [PromisesApi](promisesapi/promisesapi.md)
  Creates a `PromisesApi` object.
- [PromisesApiOptions](promisesapioptions.md)
  A dictionary of options for promises API classes.
- [Security](security.md)
  A dictionary of your authorization tokens.

## See Also

- [CancellablePromise](cancellablepromise.md)
  A promise that has a function to cancel its operation.
- [CKToolDatabaseModule](cktooldatabasemodule.md)
  The imported package that provides access to CloudKit containers and databases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cktooljs/promisesapi)*