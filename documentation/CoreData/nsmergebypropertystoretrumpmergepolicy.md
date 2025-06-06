# NSMergeByPropertyStoreTrumpMergePolicy

**Framework**: Core Data  
**Kind**: var

A property-based merge policy that applies external changes.

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
var NSMergeByPropertyStoreTrumpMergePolicy: AnyObject
```

#### Discussion

A policy that merges conflicts between the persistent store’s version of the object and the current in-memory version by individual property, with external changes trumping in-memory changes.

## See Also

- [var NSErrorMergePolicy: AnyObject](nserrormergepolicy.md)
  The default merge policy for all managed object contexts.
- [var NSMergeByPropertyObjectTrumpMergePolicy: AnyObject](nsmergebypropertyobjecttrumpmergepolicy.md)
  A property-based merge policy that applies in-memory changes.
- [var NSOverwriteMergePolicy: AnyObject](nsoverwritemergepolicy.md)
  A merge policy that overwrites the entire stored object.
- [var NSRollbackMergePolicy: AnyObject](nsrollbackmergepolicy.md)
  A merge policy that discards unsaved changes.
- [enum NSMergePolicyType](nsmergepolicytype.md)
  Constants that define merge policy types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergebypropertystoretrumpmergepolicy)*