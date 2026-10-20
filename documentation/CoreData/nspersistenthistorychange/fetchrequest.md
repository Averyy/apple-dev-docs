# fetchRequest

**Framework**: Core Data  
**Kind**: property  
**Role**: Type Property

A fetch request that has the persistent history change as the entity.

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
class var fetchRequest: NSFetchRequest<any NSFetchRequestResult>? { get }
```

```objc
@property (class, readonly, nullable) NSFetchRequest * fetchRequest;
```

## See Also

### Inspecting Change Metadata
- [class var entityDescription: NSEntityDescription?](./entitydescription.md)
  The entity description of the persistent history change entity.
- [class func entityDescription(with: NSManagedObjectContext) -> NSEntityDescription?](./entitydescription%28with%29.md)
  Requests an entity description for the managed object type affected by the change using the provided context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychange/fetchrequest)*