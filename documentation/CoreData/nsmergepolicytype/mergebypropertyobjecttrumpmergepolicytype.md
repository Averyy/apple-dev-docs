# NSMergePolicyType.mergeByPropertyObjectTrumpMergePolicyType

**Framework**: Core Data  
**Kind**: case

A property-based merge policy that applies in-memory changes.

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
case mergeByPropertyObjectTrumpMergePolicyType
```

## Mentions

- [Configuring Entities](configuring-entities.md)

#### Discussion

A policy that merges conflicts between the persistent store’s version of the object and the current in-memory version by individual property, with in-memory changes trumping external changes.

## See Also

- [NSMergePolicyType.errorMergePolicyType](nsmergepolicytype/errormergepolicytype.md)
  The default merge policy for all managed object contexts.
- [NSMergePolicyType.mergeByPropertyStoreTrumpMergePolicyType](nsmergepolicytype/mergebypropertystoretrumpmergepolicytype.md)
  A property-based merge policy that applies external changes.
- [NSMergePolicyType.overwriteMergePolicyType](nsmergepolicytype/overwritemergepolicytype.md)
  A merge policy type that overwrites the entire stored object.
- [NSMergePolicyType.rollbackMergePolicyType](nsmergepolicytype/rollbackmergepolicytype.md)
  A merge policy that discards unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergepolicytype/mergebypropertyobjecttrumpmergepolicytype)*