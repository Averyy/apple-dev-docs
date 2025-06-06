# sqlitePragmas

**Framework**: Core Data  
**Kind**: property

The SQLite pragmas set for the associated persistent store. (read-only)

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
var sqlitePragmas: [String : NSObject] { get }
```

#### Discussion

This property contains all of the pragmas set on the associated persistent store. This property is only relevant when the [`type`](nspersistentstoredescription/type.md) is set to [`NSSQLiteStoreType`](nssqlitestoretype.md).

## See Also

- [var options: [String : NSObject]](nspersistentstoredescription/options.md)
  A dictionary representation of the options set on the associated persistent store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/sqlitepragmas)*