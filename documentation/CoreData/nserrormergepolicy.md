# NSErrorMergePolicy

**Framework**: Core Data  
**Kind**: var

The default merge policy for all managed object contexts.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var NSErrorMergePolicy: AnyObject
```

#### Discussion

If a save fails because of conflicting objects, you can find the IDs of those objects in error’s `userInfo` dictionary. Use the [`NSInsertedObjectsKey`](nsinsertedobjectskey.md) and [`NSUpdatedObjectsKey`](nsupdatedobjectskey.md) keys to extract the object IDs.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nserrormergepolicy)*