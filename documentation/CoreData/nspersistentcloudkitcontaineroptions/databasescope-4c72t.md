# databaseScope

**Framework**: Core Data  
**Kind**: property

The database scope — public, private, or shared — to use for a specified store in a persistent CloudKit container.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
var databaseScope: CKDatabase.Scope { get set }
```

## See Also

- [init(containerIdentifier: String)](nspersistentcloudkitcontaineroptions/init(containeridentifier:).md)
  Initializes container options using the given CloudKit container identifier.
- [var containerIdentifier: String](nspersistentcloudkitcontaineroptions/containeridentifier.md)
  The identifier of the CloudKit container associated with a given store description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontaineroptions/databasescope-4c72t)*