# options

**Framework**: Core Data  
**Kind**: property

A dictionary representation of the options set on the associated persistent store.

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
var options: [String : NSObject] { get }
```

#### Discussion

A dictionary containing key-value pairs that specify numerous settings for the persistent store. For key definitions, see [`NSPersistentStoreCoordinator`](nspersistentstorecoordinator.md).

## See Also

- [var sqlitePragmas: [String : NSObject]](nspersistentstoredescription/sqlitepragmas.md)
  The SQLite pragmas set for the associated persistent store. (read-only)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistentstoredescription/options)*