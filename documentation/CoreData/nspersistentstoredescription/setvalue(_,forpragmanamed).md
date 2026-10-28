# setValue(_:forPragmaNamed:)

**Framework**: Core Data  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setValue:(NSObject *) value forPragmaNamed:(NSString *) name;
```

## Discussion

Pragma options are for SQLite stores only. All pragma values must be specified as [`NSString`](../../Foundation/nsstring.md)objects. The `fullfsync` and `synchronous` pragmas control the tradeoff between write performance (write to disk speed and cache utilization) and durability (data loss/corruption sensitivity to power interruption). For more information on pragma settings, see [http://sqlite.org/pragma.html](http://sqlite.org/pragma.html).

## Parameters

- `value`: The value of the pragma to be set.
- `name`: The name of the pragma to be set.

## See Also

### Configuring a Persistent Store Description
- [var url: URL?](./url.md)
  The URL that the store will use for its location.
- [var configuration: String?](./configuration.md)
  The name of the configuration used by this store.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/setvalue(_:forpragmanamed:))*