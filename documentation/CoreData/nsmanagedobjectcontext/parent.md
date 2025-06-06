# parent

**Framework**: Core Data  
**Kind**: property

The parent of the context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var parent: NSManagedObjectContext? { get set }
```

#### Discussion

`nil` indicates there is no parent context. For more details, see [`Parent store`](nsmanagedobjectcontext#Parent-store.md).

## See Also

- [var persistentStoreCoordinator: NSPersistentStoreCoordinator?](nsmanagedobjectcontext/persistentstorecoordinator.md)
  The persistent store coordinator of the context.
- [var name: String?](nsmanagedobjectcontext/name.md)
  The developer-provided name of the context.
- [var userInfo: NSMutableDictionary](nsmanagedobjectcontext/userinfo.md)
  The user information for the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/parent)*