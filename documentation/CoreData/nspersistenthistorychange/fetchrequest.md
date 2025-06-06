# fetchRequest

**Framework**: Core Data  
**Kind**: property

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

## See Also

- [class var entityDescription: NSEntityDescription?](nspersistenthistorychange/entitydescription.md)
  The entity description of the persistent history change entity.
- [class func entityDescription(with: NSManagedObjectContext) -> NSEntityDescription?](nspersistenthistorychange/entitydescription(with:).md)
  Requests an entity description for the managed object type affected by the change using the provided context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nspersistenthistorychange/fetchrequest)*