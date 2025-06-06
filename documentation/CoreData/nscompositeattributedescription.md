# NSCompositeAttributeDescription

**Framework**: Core Data  
**Kind**: class

A description of an attribute that derives its value by composing other attributes.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
class NSCompositeAttributeDescription
```

#### Overview

Composite attributes enable you to define and store complex data types, and then query, index, and apply constraints to those types. Model classes use dictionaries to represent those composites in-memory, where each dictionary contains keys corresponding to the names of the underlying attributes. You may use composite attributes anywhere you use standard attributes, including lightweight migrations and CloudKit, through [`NSPersistentCloudKitContainer`](nspersistentcloudkitcontainer.md). You can even nest composites inside other composites to create complex object hierarchies without additional model classes.

> **Note**:  Composite attributes are available only to persistent stores that you configure with the [`sqlite`](nspersistentstore/storetype/sqlite.md) store type.

 Composite attributes are available only to persistent stores that you configure with the [`sqlite`](nspersistentstore/storetype/sqlite.md) store type.

In most scenarios, prefer to use Xcode’s model editor to add composite attributes to your entities and then regenerate your model classes. However, if you need to create composites dynamically at runtime, create an instance of this class and populate its [`elements`](nscompositeattributedescription/elements.md) property with the necessary attribute descriptions.

You can access a composite’s underlying attributes using namespaced key paths and property-like setters and getters, as the following example demonstrates:

```swift
// A model class that represents the Quake entity.
class Quake: NSManagedObject {
    @NSManaged var code: String?
    @NSManaged var place: String?
    @NSManaged var date: Date?

    // A composite attribute that uses a dictionary for its in-memory storage.
    @NSManaged var magnitude: [String: Any]?
}

// Use namespaced key paths to access a composite's indvidual attributes.
let request = NSFetchRequest(entityName: "Quake")
request.predicate = NSPredicate(format: "magnitude.richter > 4.5")

// Use property-like setters and getters to manage the underlying attributes directly.
quake.magnitude.richter = 4.6
print(quake.magnitude.richter)

```

## Topics

### Composing attributes
- [var elements: [NSAttributeDescription]](nscompositeattributedescription/elements.md)
  The composed attribute descriptions.

## Relationships

### Inherits From
- [NSAttributeDescription](nsattributedescription.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSDerivedAttributeDescription](nsderivedattributedescription.md)
  A description of an attribute that derives its value by performing a calculation on a related attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nscompositeattributedescription)*