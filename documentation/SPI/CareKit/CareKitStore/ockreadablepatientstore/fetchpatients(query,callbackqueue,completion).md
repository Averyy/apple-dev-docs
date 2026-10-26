---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablepatientstore/fetchpatients(query:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchPatients(query:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`fetchPatients` asynchronously retrieves an array of patients from the store.

## Declaration

```swift
func fetchPatients(query: OCKPatientQuery, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<[Patient]>)
```

## Parameters

- `query`: A query used to constrain the values that will be fetched.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablepatientstore/fetchpatients(query:callbackqueue:completion:))*