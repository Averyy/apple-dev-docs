# init(containerIdentifier:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Initializes container options using the given CloudKit container identifier.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(containerIdentifier: String)
```

```objc
- (instancetype) initWithContainerIdentifier:(NSString *) containerIdentifier;
```

## See Also

### Creating Container Options
- [var containerIdentifier: String](./containeridentifier.md)
  The identifier of the CloudKit container associated with a given store description.
- [var databaseScope: CKDatabase.Scope](./databasescope-4c72t.md)
  The database scope — public, private, or shared — to use for a specified store in a persistent CloudKit container.
- [databaseScope](./databasescope-2784h.md)
  The database scope — public, private, or shared — to use for a specified store in a persistent CloudKit container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontaineroptions/init(containeridentifier:))*