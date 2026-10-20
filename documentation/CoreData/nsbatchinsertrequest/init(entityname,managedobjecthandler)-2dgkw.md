# init(entityName:managedObjectHandler:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
convenience init(entityName: String, managedObjectHandler handler: @escaping (NSManagedObject) -> Bool)
```

```objc
- (instancetype) initWithEntityName:(NSString *) entityName managedObjectHandler:(BOOL (^)(NSManagedObject *obj)) handler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/init(entityname:managedobjecthandler:)-2dgkw)*