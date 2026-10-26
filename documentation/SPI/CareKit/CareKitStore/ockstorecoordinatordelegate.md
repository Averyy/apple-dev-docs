---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinatordelegate"
framework: "CareKit/CareKitStore"
---

# OCKStoreCoordinatorDelegate

**Framework**: CareKit/CareKitStore  
**Kind**: protocol  
**Role**: Protocol

## Declaration

```swift
protocol OCKStoreCoordinatorDelegate : AnyObject, Sendable
```

## Topics

### Instance Methods
- [func carePlanStore(OCKAnyReadOnlyCarePlanStore, shouldHandleQuery: OCKCarePlanQuery) -> Bool](./ockstorecoordinatordelegate/careplanstore%28_,shouldhandlequery%29.md)
  Determines whether or not a store is intended to handle a given query. If true is returned, the persistent store coordinator will execute the query against the store and include the result together with results from any other stores that also respond to this query.
- [func carePlanStore(OCKAnyCarePlanStore, shouldHandleWritingCarePlan: OCKAnyCarePlan) -> Bool](./ockstorecoordinatordelegate/careplanstore%28_,shouldhandlewritingcareplan%29.md)
  Determines whether or not a store is intended to handle a certain write operation. The persistent store coordinator will call this method against all its stores in the order they were registered and execute the write on the first store that returns true for this method.
- [func contactStore(OCKAnyReadOnlyContactStore, shouldHandleQuery: OCKContactQuery) -> Bool](./ockstorecoordinatordelegate/contactstore%28_,shouldhandlequery%29.md)
  Determines whether or not a store is intended to handle a given query. If true is returned, the persistent store coordinator will execute the query against the store and include the result together with results from any other stores that also respond to this query.
- [func contactStore(OCKAnyReadOnlyContactStore, shouldHandleWritingContact: OCKAnyContact) -> Bool](./ockstorecoordinatordelegate/contactstore%28_,shouldhandlewritingcontact%29.md)
  Determines whether or not a store is intended to handle a certain write operation. The persistent store coordinator will call this method against all its stores in the order they were registered and execute the write on the first store that returns true for this method.
- [func outcomeStore(OCKAnyReadOnlyOutcomeStore, shouldHandleQuery: OCKOutcomeQuery) -> Bool](./ockstorecoordinatordelegate/outcomestore%28_,shouldhandlequery%29.md)
  Determines whether or not a store is intended to handle a given query. If true is returned, the persistent store coordinator will execute the query against the store and include the result together with results from any other stores that also respond to this query.
- [func outcomeStore(OCKAnyReadOnlyOutcomeStore, shouldHandleWritingOutcome: OCKAnyOutcome) -> Bool](./ockstorecoordinatordelegate/outcomestore%28_,shouldhandlewritingoutcome%29.md)
  Determines whether or not a store is intended to handle a certain write operation. The persistent store coordinator will call this method against all its stores in the order they were registered and execute the write on the first store that returns true for this method.
- [func patientStore(OCKAnyReadOnlyPatientStore, shouldHandleQuery: OCKPatientQuery) -> Bool](./ockstorecoordinatordelegate/patientstore%28_,shouldhandlequery%29.md)
  Determines whether or not a store is intended to handle a given query. If true is returned, the persistent store coordinator will execute the query against the store and include the result together with results from any other stores that also respond to this query.
- [func patientStore(OCKAnyPatientStore, shouldHandleWritingPatient: OCKAnyPatient) -> Bool](./ockstorecoordinatordelegate/patientstore%28_,shouldhandlewritingpatient%29.md)
  Determines whether or not a store is intended to handle a certain write operation. The persistent store coordinator will call this method against all its stores in the order they were registered and execute the write on the first store that returns true for this method.
- [func taskStore(OCKAnyReadOnlyTaskStore, shouldHandleQuery: OCKTaskQuery) -> Bool](./ockstorecoordinatordelegate/taskstore%28_,shouldhandlequery%29.md)
  Determines whether or not a store is intended to handle a given query. If true is returned, the persistent store coordinator will execute the query against the store and include the result together with results from any other stores that also respond to this query.
- [func taskStore(OCKAnyReadOnlyTaskStore, shouldHandleWritingTask: OCKAnyTask) -> Bool](./ockstorecoordinatordelegate/taskstore%28_,shouldhandlewritingtask%29.md)
  Determines whether or not a store is intended to handle a certain write operation. The persistent store coordinator will call this method against all its stores in the order they were registered and execute the write on the first store that returns true for this method.

## Relationships

### Inherits From
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [OCKStoreCoordinator](./ockstorecoordinator.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinatordelegate)*