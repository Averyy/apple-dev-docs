# init(context:)

**Framework**: Core Data  
**Kind**: init

Initializes a managed object subclass and inserts it into the specified managed object context.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
convenience init(context moc: NSManagedObjectContext)
```

#### Return Value

An initialized instance of the appropriate subclass.

#### Discussion

This method is only legal to call on subclasses of `NSManagedObject` that represent a single entity in the model.

## See Also

- [init(entity: NSEntityDescription, insertInto: NSManagedObjectContext?)](nsmanagedobject/init(entity:insertinto:).md)
  Initializes a managed object from an entity description and inserts it into the specified managed object context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsmanagedobject/init(context:))*