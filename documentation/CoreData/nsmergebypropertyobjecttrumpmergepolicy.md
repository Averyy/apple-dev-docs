# NSMergeByPropertyObjectTrumpMergePolicy

**Framework**: Core Data  
**Kind**: var

A property-based merge policy that applies in-memory changes.

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
var NSMergeByPropertyObjectTrumpMergePolicy: AnyObject
```

#### Discussion

A policy that merges conflicts between the persistent store’s version of the object and the current in-memory version by individual property, with in-memory changes trumping external changes.

## See Also

- [var NSErrorMergePolicy: AnyObject](nserrormergepolicy.md)
  The default merge policy for all managed object contexts.
- [var NSMergeByPropertyStoreTrumpMergePolicy: AnyObject](nsmergebypropertystoretrumpmergepolicy.md)
  A property-based merge policy that applies external changes.
- [var NSOverwriteMergePolicy: AnyObject](nsoverwritemergepolicy.md)
  A merge policy that overwrites the entire stored object.
- [var NSRollbackMergePolicy: AnyObject](nsrollbackmergepolicy.md)
  A merge policy that discards unsaved changes.
- [enum NSMergePolicyType](nsmergepolicytype.md)
  Constants that define merge policy types.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergebypropertyobjecttrumpmergepolicy)*