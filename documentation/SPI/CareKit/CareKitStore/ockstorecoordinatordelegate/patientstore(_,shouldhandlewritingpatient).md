---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinatordelegate/patientstore(_:shouldhandlewritingpatient:)"
framework: "CareKit/CareKitStore"
---

# patientStore(_:shouldHandleWritingPatient:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Determines whether or not a store is intended to handle a certain write operation. The persistent store coordinator will call this method against all its stores in the order they were registered and execute the write on the first store that returns true for this method.

## Declaration

```swift
func patientStore(_ store: OCKAnyPatientStore, shouldHandleWritingPatient patient: OCKAnyPatient) -> Bool
```

## Parameters

- `store`: A candidate store that should or should not handle writing.
- `patient`: The patient that needs to be written.

## Default Implementations

### OCKStoreCoordinatorDelegate Implementations
- [func patientStore(OCKAnyPatientStore, shouldHandleWritingPatient: OCKAnyPatient) -> Bool](./patientstore%28_,shouldhandlewritingpatient%29-69b1w.md)
  Determines whether or not a store is intended to handle a certain write operation. The persistent store coordinator will call this method against all its stores in the order they were registered and execute the write on the first store that returns true for this method.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinatordelegate/patientstore(_:shouldhandlewritingpatient:))*