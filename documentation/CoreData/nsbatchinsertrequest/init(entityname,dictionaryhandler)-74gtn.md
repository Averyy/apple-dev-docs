# init(entityName:dictionaryHandler:)

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
convenience init(entityName: String, dictionaryHandler handler: @escaping (NSMutableDictionary) -> Bool)
```

```objc
- (instancetype) initWithEntityName:(NSString *) entityName dictionaryHandler:(BOOL (^)(NSMutableDictionary<NSString *,id> *obj)) handler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchinsertrequest/init(entityname:dictionaryhandler:)-74gtn)*