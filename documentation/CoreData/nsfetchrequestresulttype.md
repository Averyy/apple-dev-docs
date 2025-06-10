# NSFetchRequestResultType

**Framework**: Core Data  
**Kind**: struct

Constants that specify the possible result types a fetch request can return.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct NSFetchRequestResultType
```

#### Overview

These constants are used by [`resultType`](nsfetchrequest/resulttype.md).

## Topics

### Result Types
- [static var managedObjectResultType: NSFetchRequestResultType](nsfetchrequestresulttype/managedobjectresulttype.md)
  The request returns managed objects.
- [static var managedObjectIDResultType: NSFetchRequestResultType](nsfetchrequestresulttype/managedobjectidresulttype.md)
  The request returns managed object IDs.
- [static var dictionaryResultType: NSFetchRequestResultType](nsfetchrequestresulttype/dictionaryresulttype.md)
  The request returns dictionaries.
- [static var countResultType: NSFetchRequestResultType](nsfetchrequestresulttype/countresulttype.md)
  The request returns the count of the objects that match the request.
### Initializers
- [init(rawValue: UInt)](nsfetchrequestresulttype/init(rawvalue:).md)
  Creates a fetch request result type using the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [init()](nsfetchrequest/init.md)
  Creates a new fetch request.
- [convenience init(entityName: String)](nsfetchrequest/init(entityname:).md)
  Initializes a fetch request configured with a given entity name.
- [var entityName: String?](nsfetchrequest/entityname.md)
  The name of the entity the request is configured to fetch.
- [var entity: NSEntityDescription?](nsfetchrequest/entity.md)
  The entity specified for the fetch request.
- [var includesSubentities: Bool](nsfetchrequest/includessubentities.md)
  A Boolean value that indicates whether the fetch request includes subentities in the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequestresulttype)*