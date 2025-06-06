# NSMergePolicyType.errorMergePolicyType

**Framework**: Core Data  
**Kind**: case

The default merge policy for all managed object contexts.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case errorMergePolicyType
```

#### Discussion

If a save fails because of conflicting objects, you can find the IDs of those objects in error’s `userInfo` dictionary. Use the [`NSInsertedObjectsKey`](nsinsertedobjectskey.md) and [`NSUpdatedObjectsKey`](nsupdatedobjectskey.md) keys to extract the object IDs.

## See Also

- [NSMergePolicyType.mergeByPropertyStoreTrumpMergePolicyType](nsmergepolicytype/mergebypropertystoretrumpmergepolicytype.md)
  A property-based merge policy that applies external changes.
- [NSMergePolicyType.mergeByPropertyObjectTrumpMergePolicyType](nsmergepolicytype/mergebypropertyobjecttrumpmergepolicytype.md)
  A property-based merge policy that applies in-memory changes.
- [NSMergePolicyType.overwriteMergePolicyType](nsmergepolicytype/overwritemergepolicytype.md)
  A merge policy type that overwrites the entire stored object.
- [NSMergePolicyType.rollbackMergePolicyType](nsmergepolicytype/rollbackmergepolicytype.md)
  A merge policy that discards unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergepolicytype/errormergepolicytype)*