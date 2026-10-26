---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/deleteanypatients(_:)"
framework: "CareKit/CareKitStore"
---

# deleteAnyPatients(_:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

`deleteAnyPatients` asynchronously deletes an array of patients from the store.

## Declaration

```swift
@discardableResult
func deleteAnyPatients(_ patients: [OCKAnyPatient]) async throws -> [OCKAnyPatient]
```

## Parameters

- `patients`: An array of patients to be deleted. The patients must exist in the store.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/deleteanypatients(_:))*