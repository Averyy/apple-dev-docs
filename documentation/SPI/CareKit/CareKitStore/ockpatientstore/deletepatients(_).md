---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore/deletepatients(_:)"
framework: "CareKit/CareKitStore"
---

# deletePatients(_:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

`deletePatients` asynchronously deletes an array of patients from the store.

## Declaration

```swift
@discardableResult
func deletePatients(_ patients: [Patient]) async throws -> [Patient]
```

## Parameters

- `patients`: An array of patients to be deleted. The patients must exist in the store.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockpatientstore/deletepatients(_:))*