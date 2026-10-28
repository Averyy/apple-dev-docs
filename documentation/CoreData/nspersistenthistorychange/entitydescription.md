# entityDescription

**Framework**: Core Data  
**Kind**: property  
**Role**: Type Property

The entity description of the persistent history change entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class var entityDescription: NSEntityDescription? { get }
```

```objc
@property (class, readonly, nullable) NSEntityDescription * entityDescription;
```

## Discussion

The entity description of a [`NSPersistentHistoryChange`](../nspersistenthistorychange.md), includes its properties, which can be useful for filtering your persistent history change request.

## See Also

### Inspecting Change Metadata
- [class var fetchRequest: NSFetchRequest<any NSFetchRequestResult>?](./fetchrequest.md)
  A fetch request that has the persistent history change as the entity.
- [class func entityDescription(with: NSManagedObjectContext) -> NSEntityDescription?](./entitydescription%28with%29.md)
  Requests an entity description for the managed object type affected by the change using the provided context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychange/entitydescription)*