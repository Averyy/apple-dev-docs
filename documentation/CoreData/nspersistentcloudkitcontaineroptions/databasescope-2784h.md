# databaseScope

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The database scope — public, private, or shared — to use for a specified store in a persistent CloudKit container.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```objc
@property (nonatomic) CKDatabaseScope databaseScope;
```

## See Also

### Creating Container Options
- [init(containerIdentifier: String)](./init%28containeridentifier%29.md)
  Initializes container options using the given CloudKit container identifier.
- [var containerIdentifier: String](./containeridentifier.md)
  The identifier of the CloudKit container associated with a given store description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontaineroptions/databasescope-2784h)*