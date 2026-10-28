# NSMergePolicyType.overwriteMergePolicyType

**Framework**: Core Data  
**Kind**: case  
**Role**: Case

A merge policy type that overwrites the entire stored object.

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
case overwriteMergePolicyType
```

```c
NSOverwriteMergePolicyType
```

## Discussion

This policy merges conflicts between the persistent store’s version of the object and the current in-memory version by saving the entire in-memory object to the persistent store.

## See Also

### Policies
- [NSMergePolicyType.errorMergePolicyType](./errormergepolicytype.md)
  The default merge policy for all managed object contexts.
- [NSMergePolicyType.mergeByPropertyStoreTrumpMergePolicyType](./mergebypropertystoretrumpmergepolicytype.md)
  A property-based merge policy that applies external changes.
- [NSMergePolicyType.mergeByPropertyObjectTrumpMergePolicyType](./mergebypropertyobjecttrumpmergepolicytype.md)
  A property-based merge policy that applies in-memory changes.
- [NSMergePolicyType.rollbackMergePolicyType](./rollbackmergepolicytype.md)
  A merge policy that discards unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergepolicytype/overwritemergepolicytype)*