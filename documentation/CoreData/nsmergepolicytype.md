# NSMergePolicyType

**Framework**: Core Data  
**Kind**: enum

Constants that define merge policy types.

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
enum NSMergePolicyType
```

## Topics

### Policies
- [NSMergePolicyType.errorMergePolicyType](nsmergepolicytype/errormergepolicytype.md)
  The default merge policy for all managed object contexts.
- [NSMergePolicyType.mergeByPropertyStoreTrumpMergePolicyType](nsmergepolicytype/mergebypropertystoretrumpmergepolicytype.md)
  A property-based merge policy that applies external changes.
- [NSMergePolicyType.mergeByPropertyObjectTrumpMergePolicyType](nsmergepolicytype/mergebypropertyobjecttrumpmergepolicytype.md)
  A property-based merge policy that applies in-memory changes.
- [NSMergePolicyType.overwriteMergePolicyType](nsmergepolicytype/overwritemergepolicytype.md)
  A merge policy type that overwrites the entire stored object.
- [NSMergePolicyType.rollbackMergePolicyType](nsmergepolicytype/rollbackmergepolicytype.md)
  A merge policy that discards unsaved changes.
### Initializers
- [init?(rawValue: UInt)](nsmergepolicytype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var NSErrorMergePolicy: AnyObject](nserrormergepolicy.md)
  The default merge policy for all managed object contexts.
- [var NSMergeByPropertyStoreTrumpMergePolicy: AnyObject](nsmergebypropertystoretrumpmergepolicy.md)
  A property-based merge policy that applies external changes.
- [var NSMergeByPropertyObjectTrumpMergePolicy: AnyObject](nsmergebypropertyobjecttrumpmergepolicy.md)
  A property-based merge policy that applies in-memory changes.
- [var NSOverwriteMergePolicy: AnyObject](nsoverwritemergepolicy.md)
  A merge policy that overwrites the entire stored object.
- [var NSRollbackMergePolicy: AnyObject](nsrollbackmergepolicy.md)
  A merge policy that discards unsaved changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmergepolicytype)*