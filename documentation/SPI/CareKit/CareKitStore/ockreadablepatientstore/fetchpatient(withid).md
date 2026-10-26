---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablepatientstore/fetchpatient(withid:)"
framework: "CareKit/CareKitStore"
---

# fetchPatient(withID:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

`fetchPatient` asynchronously fetches a single patient from the store using its user-defined identifier. If a patient with the specified identifier does not exist, the completion handler will be called with an error.

## Declaration

```swift
func fetchPatient(withID id: String) async throws -> Patient
```

## Parameters

- `id`: The identifier of the item to be fetched.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablepatientstore/fetchpatient(withid:))*