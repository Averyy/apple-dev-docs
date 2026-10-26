# batchUpdateRequestWithEntityName:

**Framework**: Core Data  
**Kind**: method  
**Role**: Type Method

Creates a batch-update request for a named managed entity.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```objc
+ (instancetype) batchUpdateRequestWithEntityName:(NSString *) entityName;
```

#### Return Value

A batch-update request.

## Parameters

- `entityName`: The name of the managed entity to update data for.

## See Also

### Creating a Request
- [init(entity: NSEntityDescription)](./init%28entity%29.md)
  Creates a batch-update request for a managed entity.
- [init(entityName: String)](./init%28entityname%29.md)
  Creates a batch-update request for a named managed entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsbatchupdaterequest/batchupdaterequestwithentityname:)*