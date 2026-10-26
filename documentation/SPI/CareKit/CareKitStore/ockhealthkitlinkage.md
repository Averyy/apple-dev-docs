---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkitlinkage"
framework: "CareKit/CareKitStore"
---

# OCKHealthKitLinkage

**Framework**: CareKit/CareKitStore  
**Kind**: struct  
**Role**: Structure

Describes how a task outcome values should be retrieved from HealthKit.

## Declaration

```swift
struct OCKHealthKitLinkage
```

## Topics

### Initializers
- [init(from: any Decoder) throws](./ockhealthkitlinkage/init%28from%29.md)
- [init(quantityIdentifier: HKQuantityTypeIdentifier, quantityType: QuantityType, unit: HKUnit)](./ockhealthkitlinkage/init%28quantityidentifier,quantitytype,unit%29.md)
  Initialize by specifying HealthKit types.
### Instance Properties
- [var quantityIdentifier: HKQuantityTypeIdentifier](./ockhealthkitlinkage/quantityidentifier.md)
  A HealthKitQuantityIdentifier that describes the outcome’s data type.
- [var quantityType: QuantityType](./ockhealthkitlinkage/quantitytype-swift.property.md)
  Determines what kind of query will be used to fetch data from HealthKit.
- [var unit: HKUnit](./ockhealthkitlinkage/unit.md)
  A HealthKit unit that will be associated with outcomes saved to and fetched from HealthKit.
### Enumerations
- [OCKHealthKitLinkage.QuantityType](./ockhealthkitlinkage/quantitytype-swift.enum.md)
### Default Implementations
- [Equatable Implementations](./ockhealthkitlinkage/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Care tasks
- [struct OCKTask](./ocktask.md)
  An `OCKTask` represents some task or action that a patient is supposed to perform. Tasks are optionally associable with an `OCKCarePlan` and must have a unique id and schedule. The schedule determines when and how often the task should be performed, and the `impactsAdherence` flag may be used to specify whether or not the patients adherence to this task will affect their daily completion rings.
- [protocol OCKAnyTask](./ockanytask.md)
  Conforming a type to `OCKAnyTask` allows it to be queried and displayed by CareKit.
- [protocol OCKAnyVersionableTask](./ockanyversionabletask.md)
  Any task that has a notion of versioning and is persisted in a database. Conforming a store’s task type to this protocol allows CareKit to provide default implementations for `OCKReadOnlyEventStore` methods.
- [struct OCKHealthKitTask](./ockhealthkittask.md)
  An `OCKHealthKitTask` represents some task or action that a patient is supposed to perform. Tasks are optionally associable with an `OCKCarePlan` and must have a unique id and schedule. The schedule determines when and how often the task should be performed, and the `impactsAdherence` flag may be used to specify whether or not the patients adherence to this task will affect their daily completion rings.
- [protocol OCKTaskStore](./ocktaskstore.md)
  Any store that can perform read and write operations on a single type conforming to `OCKAnyTask` is considered an `OCKTaskStore`.
- [protocol OCKAnyTaskStore](./ockanytaskstore.md)
  Any store able to write to one ore more types conforming to `OCKAnyTask` is considered an `OCKAnyTaskStore`.
- [protocol OCKReadableTaskStore](./ockreadabletaskstore.md)
  A store that allows for reading tasks.
- [protocol OCKAnyReadOnlyTaskStore](./ockanyreadonlytaskstore.md)
  A store that allows for reading tasks.
- [struct OCKTaskQuery](./ocktaskquery.md)
  A query that limits which tasks will be returned when fetching.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkitlinkage)*