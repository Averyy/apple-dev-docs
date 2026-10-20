# NSMergePolicyType.mergeByPropertyObjectTrumpMergePolicyType

**Framework**: Core Data  
**Kind**: case  
**Role**: Case

A property-based merge policy that applies in-memory changes.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case mergeByPropertyObjectTrumpMergePolicyType
```

```c
NSMergeByPropertyObjectTrumpMergePolicyType
```

## Mentions

- [Configuring Entities](../configuring-entities.md)

#### Discussion

A policy that merges conflicts between the persistent store’s version of the object and the current in-memory version by individual property, with in-memory changes trumping external changes.

## See Also

### Policies
- [NSMergePolicyType.errorMergePolicyType](./errormergepolicytype.md)
  The default merge policy for all managed object contexts.
- [NSMergePolicyType.mergeByPropertyStoreTrumpMergePolicyType](./mergebypropertystoretrumpmergepolicytype.md)
  A property-based merge policy that applies external changes.
- [NSMergePolicyType.overwriteMergePolicyType](./overwritemergepolicytype.md)
  A merge policy type that overwrites the entire stored object.
- [NSMergePolicyType.rollbackMergePolicyType](./rollbackmergepolicytype.md)
  A merge policy that discards unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergepolicytype/mergebypropertyobjecttrumpmergepolicytype)*