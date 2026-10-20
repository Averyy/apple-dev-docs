# init(entity:)

**Framework**: Core Data  
**Kind**: init  
**Role**: Initializer

Creates a batch-update request for a managed entity.

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
init(entity: NSEntityDescription)
```

```objc
- (instancetype) initWithEntity:(NSEntityDescription *) entity;
```

## Parameters

- `entity`: The managed entity to update data for.

## See Also

### Creating a Request
- [init(entityName: String)](./init%28entityname%29.md)
  Creates a batch-update request for a named managed entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/init(entity:))*