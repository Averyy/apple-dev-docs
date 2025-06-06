# NSMergePolicyType.rollbackMergePolicyType

**Framework**: Core Data  
**Kind**: case

A merge policy that discards unsaved changes.

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
case rollbackMergePolicyType
```

#### Discussion

This policy merges conflicts between the persistent store’s version of the object and the current in-memory version by discarding unsaved changes.

## See Also

- [NSMergePolicyType.errorMergePolicyType](nsmergepolicytype/errormergepolicytype.md)
  The default merge policy for all managed object contexts.
- [NSMergePolicyType.mergeByPropertyStoreTrumpMergePolicyType](nsmergepolicytype/mergebypropertystoretrumpmergepolicytype.md)
  A property-based merge policy that applies external changes.
- [NSMergePolicyType.mergeByPropertyObjectTrumpMergePolicyType](nsmergepolicytype/mergebypropertyobjecttrumpmergepolicytype.md)
  A property-based merge policy that applies in-memory changes.
- [NSMergePolicyType.overwriteMergePolicyType](nsmergepolicytype/overwritemergepolicytype.md)
  A merge policy type that overwrites the entire stored object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergepolicytype/rollbackmergepolicytype)*