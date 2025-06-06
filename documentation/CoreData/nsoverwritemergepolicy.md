# NSOverwriteMergePolicy

**Framework**: Core Data  
**Kind**: var

A merge policy that overwrites the entire stored object.

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
var NSOverwriteMergePolicy: AnyObject
```

#### Discussion

This policy merges conflicts between the persistent store’s version of the object and the current in-memory version by saving the entire in-memory object to the persistent store.

## See Also

- [var NSErrorMergePolicy: AnyObject](nserrormergepolicy.md)
  The default merge policy for all managed object contexts.
- [var NSMergeByPropertyStoreTrumpMergePolicy: AnyObject](nsmergebypropertystoretrumpmergepolicy.md)
  A property-based merge policy that applies external changes.
- [var NSMergeByPropertyObjectTrumpMergePolicy: AnyObject](nsmergebypropertyobjecttrumpmergepolicy.md)
  A property-based merge policy that applies in-memory changes.
- [var NSRollbackMergePolicy: AnyObject](nsrollbackmergepolicy.md)
  A merge policy that discards unsaved changes.
- [enum NSMergePolicyType](nsmergepolicytype.md)
  Constants that define merge policy types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsoverwritemergepolicy)*