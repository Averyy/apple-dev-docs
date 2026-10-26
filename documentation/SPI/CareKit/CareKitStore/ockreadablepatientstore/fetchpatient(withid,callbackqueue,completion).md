---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablepatientstore/fetchpatient(withid:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchPatient(withID:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`fetchPatient` asynchronously fetches a single patient from the store using its user-defined identifier. If a patient with the specified identifier does not exist, the completion handler will be called with an error.

## Declaration

```swift
func fetchPatient(withID id: String, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<Patient>)
```

## Parameters

- `id`: A unique user-defined identifier
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKReadablePatientStore Implementations
- [func fetchPatient(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<Patient>)](./fetchpatient%28withid,callbackqueue,completion%29-8y7h1.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablepatientstore/fetchpatient(withid:callbackqueue:completion:))*