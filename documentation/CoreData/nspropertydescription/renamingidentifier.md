# renamingIdentifier

**Framework**: Core Data  
**Kind**: property

The renaming identifier for the receiver.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var renamingIdentifier: String? { get set }
```

#### Discussion

This is used to resolve naming conflicts between models. When creating an entity mapping between entities in two managed object models, a source entity property and a destination entity property that share the same identifier indicate that a property mapping should be configured to migrate from the source to the destination. If unset, the identifier will return the property’s name.

## See Also

- [var versionHash: Data](nspropertydescription/versionhash.md)
  The version hash for the receiver.
- [var versionHashModifier: String?](nspropertydescription/versionhashmodifier.md)
  The version hash modifier for the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspropertydescription/renamingidentifier)*