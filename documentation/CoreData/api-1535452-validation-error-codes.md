# Validation error codes

**Framework**: Core Data

Error codes relating to the validation of managed objects.

#### Overview

For additional error codes, including `NSValidationErrorMinimum` and `NSValidationErrorMaximum`, see [`NSError`](https://developer.apple.com/documentation/Foundation/NSError).

## Topics

### Error codes
- [var NSCoreDataError: Int](nscoredataerror.md)
  An error code that indicates a nonspecific Core Data error.
- [var NSEntityMigrationPolicyError: Int](nsentitymigrationpolicyerror.md)
  An error code that indicates a migration failure during processing of an entity migration policy.
- [var NSExternalRecordImportError: Int](nsexternalrecordimporterror.md)
  Error code to denote a general error encountered while importing external records.
- [var NSInferredMappingModelError: Int](nsinferredmappingmodelerror.md)
  Error code to denote a problem with the creation of an inferred mapping model.
- [var NSManagedObjectConstraintMergeError: Int](nsmanagedobjectconstraintmergeerror.md)
  Error code to denote a problem with the merging of instances of a managed object.
- [var NSManagedObjectConstraintValidationError: Int](nsmanagedobjectconstraintvalidationerror.md)
  Error code to denote a problem with the validation of a managed object.
- [var NSManagedObjectContextLockingError: Int](nsmanagedobjectcontextlockingerror.md)
  Error code to denote an inability to acquire a lock in a managed object context.
- [var NSManagedObjectExternalRelationshipError: Int](nsmanagedobjectexternalrelationshiperror.md)
  Error code to denote that an object being saved has a relationship containing an object from another store.
- [var NSManagedObjectMergeError: Int](nsmanagedobjectmergeerror.md)
  Error code to denote that a merge policy failed—Core Data is unable to complete merging.
- [var NSManagedObjectModelReferenceNotFoundError: Int](nsmanagedobjectmodelreferencenotfounderror.md)
  An error code that indicates Core Data isn’t able to find or instantiate the referenced object model.
- [var NSManagedObjectReferentialIntegrityError: Int](nsmanagedobjectreferentialintegrityerror.md)
  Error code to denote an attempt to fire a fault pointing to an object that does not exist.
- [var NSManagedObjectValidationError: Int](nsmanagedobjectvalidationerror.md)
  Error code to denote a generic validation error.
- [var NSMigrationCancelledError: Int](nsmigrationcancellederror.md)
  Error code to denote that migration failed due to manual cancellation.
- [var NSMigrationConstraintViolationError: Int](nsmigrationconstraintviolationerror.md)
  Error code to denote a problem with the validation of a managed object during a migration.
- [var NSMigrationError: Int](nsmigrationerror.md)
  Error code to denote a general migration error.
- [var NSMigrationManagerDestinationStoreError: Int](nsmigrationmanagerdestinationstoreerror.md)
  Error code to denote that migration failed due to a problem with the destination data store.
- [var NSMigrationManagerSourceStoreError: Int](nsmigrationmanagersourcestoreerror.md)
  Error code to denote that migration failed due to a problem with the source data store.
- [var NSMigrationMissingMappingModelError: Int](nsmigrationmissingmappingmodelerror.md)
  Error code to denote that migration failed due to a missing mapping model.
- [var NSMigrationMissingSourceModelError: Int](nsmigrationmissingsourcemodelerror.md)
  Error code to denote that migration failed due to a missing source data model.
- [var NSPersistentHistoryTokenExpiredError: Int](nspersistenthistorytokenexpirederror.md)
  Error code to denote that the persistent history token has expired.
- [var NSPersistentStoreCoordinatorLockingError: Int](nspersistentstorecoordinatorlockingerror.md)
  Error code to denote an inability to acquire a lock in a persistent store.
- [var NSPersistentStoreIncompatibleSchemaError: Int](nspersistentstoreincompatibleschemaerror.md)
  Error code to denote that a persistent store returned an error for a save operation.
- [var NSPersistentStoreIncompatibleVersionHashError: Int](nspersistentstoreincompatibleversionhasherror.md)
  Error code to denote that entity version hashes in the store are incompatible with the current managed object model.
- [var NSPersistentStoreIncompleteSaveError: Int](nspersistentstoreincompletesaveerror.md)
  Error code to denote that one or more of the stores returned an error during a save operations.
- [var NSPersistentStoreInvalidTypeError: Int](nspersistentstoreinvalidtypeerror.md)
  Error code to denote an unknown persistent store type/format/version.
- [var NSPersistentStoreOpenError: Int](nspersistentstoreopenerror.md)
  Error code to denote an error occurred while attempting to open a persistent store.
- [var NSPersistentStoreOperationError: Int](nspersistentstoreoperationerror.md)
  Error code to denote that a persistent store operation failed.
- [var NSPersistentStoreSaveConflictsError: Int](nspersistentstoresaveconflictserror.md)
  Error code to denote that an unresolved merge conflict was encountered during a save. .
- [var NSPersistentStoreSaveError: Int](nspersistentstoresaveerror.md)
  Error code to denote that a persistent store returned an error for a save operation.
- [var NSPersistentStoreTimeoutError: Int](nspersistentstoretimeouterror.md)
  Error code to denote that Core Data failed to connect to a persistent store within the time specified by `NSPersistentStoreTimeoutOption`.
- [var NSPersistentStoreTypeMismatchError: Int](nspersistentstoretypemismatcherror.md)
  Error code returned by a persistent store coordinator if a store is accessed that does not match the specified type.
- [var NSPersistentStoreUnsupportedRequestTypeError: Int](nspersistentstoreunsupportedrequesttypeerror.md)
  Error code to denote that an `NSPersistentStore` subclass was passed a request (an instance of [`NSPersistentStoreRequest`](nspersistentstorerequest.md)) that it did not understand.
- [var NSSQLiteError: Int](nssqliteerror.md)
  Error code to denote a general SQLite error.
- [var NSStagedMigrationBackwardMigrationError: Int](nsstagedmigrationbackwardmigrationerror.md)
  An error code that indicates a failed migration because of an attempt to migrate backward.
- [var NSStagedMigrationFrameworkVersionMismatchError: Int](nsstagedmigrationframeworkversionmismatcherror.md)
  An error code that indicates a failed migration because the persistent store’s metadata doesn’t support staged lightweight migrations.
- [var NSValidationInvalidURIError: Int](nsvalidationinvalidurierror.md)
  Error code to denote a problem with the validation of a URI property.
- [var NSValidationMultipleErrorsError: Int](nsvalidationmultipleerrorserror.md)
  Error code to denote an error containing multiple validation errors.
- [var NSValidationMissingMandatoryPropertyError: Int](nsvalidationmissingmandatorypropertyerror.md)
  Error code for a non-optional property with a nil value.
- [var NSValidationRelationshipLacksMinimumCountError: Int](nsvalidationrelationshiplacksminimumcounterror.md)
  Error code to denote a to-many relationship with too few destination objects.
- [var NSValidationRelationshipExceedsMaximumCountError: Int](nsvalidationrelationshipexceedsmaximumcounterror.md)
  Error code to denote a bounded to-many relationship with too many destination objects.
- [var NSValidationRelationshipDeniedDeleteError: Int](nsvalidationrelationshipdenieddeleteerror.md)
  Error code to denote some relationship with delete rule `NSDeleteRuleDeny` is non-empty.
- [var NSValidationNumberTooLargeError: Int](nsvalidationnumbertoolargeerror.md)
  Error code to denote some numerical value is too large.
- [var NSValidationNumberTooSmallError: Int](nsvalidationnumbertoosmallerror.md)
  Error code to denote some numerical value is too small.
- [var NSValidationDateTooLateError: Int](nsvalidationdatetoolateerror.md)
  Error code to denote some date value is too late.
- [var NSValidationDateTooSoonError: Int](nsvalidationdatetoosoonerror.md)
  Error code to denote some date value is too soon.
- [var NSValidationInvalidDateError: Int](nsvalidationinvaliddateerror.md)
  Error code to denote some date value fails to match date pattern.
- [var NSValidationStringTooLongError: Int](nsvalidationstringtoolongerror.md)
  Error code to denote some string value is too long.
- [var NSValidationStringTooShortError: Int](nsvalidationstringtooshorterror.md)
  Error code to denote some string value is too short.
- [var NSValidationStringPatternMatchingError: Int](nsvalidationstringpatternmatchingerror.md)
  Error code to denote some string value fails to match some pattern.

## See Also

- [func validateValue(AutoreleasingUnsafeMutablePointer<AnyObject?>, forKey: String) throws](nsmanagedobject/validatevalue(_:forkey:).md)
  Validates a property value for a given key.
- [func validateForDelete() throws](nsmanagedobject/validatefordelete.md)
  Determines whether the managed object can be deleted in its current state.
- [func validateForInsert() throws](nsmanagedobject/validateforinsert.md)
  Determines whether the managed object can be inserted in its current state.
- [func validateForUpdate() throws](nsmanagedobject/validateforupdate.md)
  Determines whether the managed object’s current state is valid.
- [let NSValidationKeyErrorKey: String](nsvalidationkeyerrorkey.md)
  The error key for the attribute that failed to validate.
- [let NSValidationObjectErrorKey: String](nsvalidationobjecterrorkey.md)
  The error key for the object that failed to validate.
- [let NSValidationPredicateErrorKey: String](nsvalidationpredicateerrorkey.md)
  The error key for the predicate that failed to validate.
- [let NSValidationValueErrorKey: String](nsvalidationvalueerrorkey.md)
  The error key for the value that failed to validate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/1535452-validation-error-codes)*