# parent

**Framework**: Core Data  
**Kind**: property  
**Role**: Instance Property

The parent of the context.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var parent: NSManagedObjectContext? { get set }
```

```objc
@property (strong, nullable) NSManagedObjectContext * parentContext;
```

## Discussion

`nil` indicates there is no parent context. For more details, see [Parent store](../nsmanagedobjectcontext.md#Parent-store).

## See Also

### Configuring a context
- [var persistentStoreCoordinator: NSPersistentStoreCoordinator?](./persistentstorecoordinator.md)
  The persistent store coordinator of the context.
- [var name: String?](./name.md)
  The developer-provided name of the context.
- [var userInfo: NSMutableDictionary](./userinfo.md)
  The user information for the context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/parent)*