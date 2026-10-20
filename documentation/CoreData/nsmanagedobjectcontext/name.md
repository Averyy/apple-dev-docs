# name

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The developer-provided name of the context.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String? { get set }
```

```objc
@property (copy, nullable) NSString * name;
```

## Mentions

- [Consuming relevant store changes](../consuming-relevant-store-changes.md)

## See Also

### Configuring a context
- [var persistentStoreCoordinator: NSPersistentStoreCoordinator?](./persistentstorecoordinator.md)
  The persistent store coordinator of the context.
- [var parent: NSManagedObjectContext?](./parent.md)
  The parent of the context.
- [var userInfo: NSMutableDictionary](./userinfo.md)
  The user information for the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/name)*