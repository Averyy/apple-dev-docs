---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlypatientstore/fetchanypatients(query:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchAnyPatients(query:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`fetchAnyPatients` asynchronously retrieves an array of patients from the store.

## Declaration

```swift
func fetchAnyPatients(query: OCKPatientQuery, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<[OCKAnyPatient]>)
```

## Parameters

- `query`: A query used to constrain the values that will be fetched.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyReadOnlyPatientStore Implementations
- [func fetchAnyPatients(query: OCKPatientQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyPatient]>)](./fetchanypatients%28query,callbackqueue,completion%29-5jlao.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlypatientstore/fetchanypatients(query:callbackqueue:completion:))*