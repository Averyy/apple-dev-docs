# persistentStoreCoordinator

**Framework**: Core Data  
**Kind**: property

The persistent store coordinator of the context.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var persistentStoreCoordinator: NSPersistentStoreCoordinator? { get set }
```

#### Return Value

The persistent store coordinator of the receiver.

#### Discussion

The coordinator provides the managed object model and handles persistency. Note that multiple contexts can share a coordinator. May not be `nil`.

Setting [`persistentStoreCoordinator`](nsmanagedobjectcontext/persistentstorecoordinator.md) to `nil` will raise an exception. If you want to “disconnect” a context from its persistent store coordinator, you should simply set all strong references to the context to `nil` and allow it to be deallocated normally.

For more details, see [`Parent store`](nsmanagedobjectcontext#Parent-store.md).

## See Also

- [var parent: NSManagedObjectContext?](nsmanagedobjectcontext/parent.md)
  The parent of the context.
- [var name: String?](nsmanagedobjectcontext/name.md)
  The developer-provided name of the context.
- [var userInfo: NSMutableDictionary](nsmanagedobjectcontext/userinfo.md)
  The user information for the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/persistentstorecoordinator)*