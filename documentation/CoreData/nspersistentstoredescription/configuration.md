# configuration

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The name of the configuration used by this store.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var configuration: String? { get set }
```

```objc
@property (copy, nullable) NSString * configuration;
```

#### Discussion

This displays the name of a configuration in the receiver’s managed object model that will be used by the new store. The configuration can be `nil`, in which case no other configurations are allowed.

## See Also

### Configuring a Persistent Store Description
- [var url: URL?](./url.md)
  The URL that the store will use for its location.
- [var timeout: TimeInterval](./timeout.md)
  The connection timeout for the associated store.
- [var type: String](./type.md)
  The type of store this description represents.
- [var isReadOnly: Bool](./isreadonly.md)
  A flag that indicates whether this store will be read-only.
- [var shouldAddStoreAsynchronously: Bool](./shouldaddstoreasynchronously.md)
  A flag that determines whether the store is added asynchronously.
- [var shouldInferMappingModelAutomatically: Bool](./shouldinfermappingmodelautomatically.md)
  A flag indicating whether a mapping model should be created automatically.
- [var shouldMigrateStoreAutomatically: Bool](./shouldmigratestoreautomatically.md)
  A flag indicating whether the associated persistent store should be migrated automatically.
- [func setOption(NSObject?, forKey: String)](./setoption%28_,forkey%29.md)
  Sets an option on the store.
- [func setValue(NSObject?, forPragmaNamed: String)](./setvalue%28_,forpragmanamed%29.md)
  Allows you to set pragmas for the SQLite store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/configuration)*