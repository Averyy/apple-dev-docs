# Merge Policies

**Framework**: Core Data

Define standard ways to handle conflicts during a save operation.

#### Overview

`NSErrorMergePolicy` is the default policy. It is the only policy that requires action to correct any conflicts. The other policies make a save go through silently by making changes that follow rules specific to that policy.

## Topics

### Policies
- [var NSErrorMergePolicy: AnyObject](nserrormergepolicy.md)
  The default merge policy for all managed object contexts.
- [var NSMergeByPropertyStoreTrumpMergePolicy: AnyObject](nsmergebypropertystoretrumpmergepolicy.md)
  A property-based merge policy that applies external changes.
- [var NSMergeByPropertyObjectTrumpMergePolicy: AnyObject](nsmergebypropertyobjecttrumpmergepolicy.md)
  A property-based merge policy that applies in-memory changes.
- [var NSOverwriteMergePolicy: AnyObject](nsoverwritemergepolicy.md)
  A merge policy that overwrites the entire stored object.
- [var NSRollbackMergePolicy: AnyObject](nsrollbackmergepolicy.md)
  A merge policy that discards unsaved changes.
- [enum NSMergePolicyType](nsmergepolicytype.md)
  Constants that define merge policy types.

## See Also

- [class var error: NSMergePolicy](nsmergepolicy/error.md)
  The default merge policy for all managed object contexts.
- [class var mergeByPropertyStoreTrump: NSMergePolicy](nsmergepolicy/mergebypropertystoretrump.md)
  A property-based merge policy that applies external changes.
- [class var mergeByPropertyObjectTrump: NSMergePolicy](nsmergepolicy/mergebypropertyobjecttrump.md)
  A property-based merge policy that applies in-memory changes.
- [class var overwrite: NSMergePolicy](nsmergepolicy/overwrite.md)
  A merge policy that overwrites the entire stored object.
- [class var rollback: NSMergePolicy](nsmergepolicy/rollback.md)
  A merge policy that discards unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/merge-policies)*