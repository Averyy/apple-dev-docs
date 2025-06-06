# setValue(_:forPragmaNamed:)

**Framework**: Core Data  
**Kind**: method

Allows you to set pragmas for the SQLite store.

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
func setValue(_ value: NSObject?, forPragmaNamed name: String)
```

#### Discussion

Pragma options are for SQLite stores only. All pragma values must be specified as [`NSString`](https://developer.apple.com/documentation/Foundation/NSString)objects. The `fullfsync` and `synchronous` pragmas control the tradeoff between write performance (write to disk speed and cache utilization) and durability (data loss/corruption sensitivity to power interruption). For more information on pragma settings, see [`http://sqlite.org/pragma.html`](https://developer.apple.comhttp://sqlite.org/pragma.html).

## Parameters

- `value`: The value of the pragma to be set.
- `name`: The name of the pragma to be set.

## See Also

- [var url: URL?](nspersistentstoredescription/url.md)
  The URL that the store will use for its location.
- [var configuration: String?](nspersistentstoredescription/configuration.md)
  The name of the configuration used by this store.
- [var timeout: TimeInterval](nspersistentstoredescription/timeout.md)
  The connection timeout for the associated store.
- [var type: String](nspersistentstoredescription/type.md)
  The type of store this description represents.
- [var isReadOnly: Bool](nspersistentstoredescription/isreadonly.md)
  A flag that indicates whether this store will be read-only.
- [var shouldAddStoreAsynchronously: Bool](nspersistentstoredescription/shouldaddstoreasynchronously.md)
  A flag that determines whether the store is added asynchronously.
- [var shouldInferMappingModelAutomatically: Bool](nspersistentstoredescription/shouldinfermappingmodelautomatically.md)
  A flag indicating whether a mapping model should be created automatically.
- [var shouldMigrateStoreAutomatically: Bool](nspersistentstoredescription/shouldmigratestoreautomatically.md)
  A flag indicating whether the associated persistent store should be migrated automatically.
- [func setOption(NSObject?, forKey: String)](nspersistentstoredescription/setoption(_:forkey:).md)
  Sets an option on the store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/setvalue(_:forpragmanamed:))*