# NSMergePolicyType.mergeByPropertyStoreTrumpMergePolicyType

**Framework**: Core Data  
**Kind**: case  
**Role**: Case

A property-based merge policy that applies external changes.

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
case mergeByPropertyStoreTrumpMergePolicyType
```

```c
NSMergeByPropertyStoreTrumpMergePolicyType
```

#### Discussion

A policy that merges conflicts between the persistent store’s version of the object and the current in-memory version by individual property, with external changes trumping in-memory changes.

## See Also

### Policies
- [NSMergePolicyType.errorMergePolicyType](./errormergepolicytype.md)
  The default merge policy for all managed object contexts.
- [NSMergePolicyType.mergeByPropertyObjectTrumpMergePolicyType](./mergebypropertyobjecttrumpmergepolicytype.md)
  A property-based merge policy that applies in-memory changes.
- [NSMergePolicyType.overwriteMergePolicyType](./overwritemergepolicytype.md)
  A merge policy type that overwrites the entire stored object.
- [NSMergePolicyType.rollbackMergePolicyType](./rollbackmergepolicytype.md)
  A merge policy that discards unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergepolicytype/mergebypropertystoretrumpmergepolicytype)*