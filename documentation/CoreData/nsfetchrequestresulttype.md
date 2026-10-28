# NSFetchRequestResultType

**Framework**: Core Data  
**Kind**: struct  
**Role**: Structure

Constants that specify the possible result types a fetch request can return.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct NSFetchRequestResultType
```

```c
enum NSFetchRequestResultType : NSUInteger;
```

## Overview

These constants are used by [`resultType`](./nsfetchrequest/resulttype.md).

## Topics

### Result Types
- [static var managedObjectResultType: NSFetchRequestResultType](./nsfetchrequestresulttype/managedobjectresulttype.md)
  The request returns managed objects.
- [static var managedObjectIDResultType: NSFetchRequestResultType](./nsfetchrequestresulttype/managedobjectidresulttype.md)
  The request returns managed object IDs.
- [static var dictionaryResultType: NSFetchRequestResultType](./nsfetchrequestresulttype/dictionaryresulttype.md)
  The request returns dictionaries.
- [static var countResultType: NSFetchRequestResultType](./nsfetchrequestresulttype/countresulttype.md)
  The request returns the count of the objects that match the request.
### Initializers
- [init(rawValue: UInt)](./nsfetchrequestresulttype/init%28rawvalue%29.md)
  Creates a fetch request result type using the specified raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Managing the Fetch Request’s Entity
- [convenience init(entityName: String)](./nsfetchrequest/init%28entityname%29-5anoo.md)
  Returns a fetch request configured with a given entity name.
- [init()](./nsfetchrequest/init%28%29.md)
  Creates a new fetch request.
- [var entityName: String?](./nsfetchrequest/entityname.md)
  The name of the entity the request is configured to fetch.
- [var entity: NSEntityDescription?](./nsfetchrequest/entity.md)
  The entity specified for the fetch request.
- [var includesSubentities: Bool](./nsfetchrequest/includessubentities.md)
  A Boolean value that indicates whether the fetch request includes subentities in the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coredata/nsfetchrequestresulttype)*