# containerIdentifier

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The identifier of the CloudKit container associated with a given store description.

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
var containerIdentifier: String { get }
```

```objc
@property (copy, readonly) NSString * containerIdentifier;
```

## See Also

### Creating Container Options
- [init(containerIdentifier: String)](./init%28containeridentifier%29.md)
  Initializes container options using the given CloudKit container identifier.
- [var databaseScope: CKDatabase.Scope](./databasescope-4c72t.md)
  The database scope — public, private, or shared — to use for a specified store in a persistent CloudKit container.
- [databaseScope](./databasescope-2784h.md)
  The database scope — public, private, or shared — to use for a specified store in a persistent CloudKit container.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentcloudkitcontaineroptions/containeridentifier)*