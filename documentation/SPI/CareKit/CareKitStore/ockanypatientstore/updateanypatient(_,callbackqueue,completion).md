---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatientstore/updateanypatient(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateAnyPatient(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`updateAnyPatient` asynchronously updates a single patient in the store.

## Declaration

```swift
func updateAnyPatient(_ patient: OCKAnyPatient, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyPatient>?)
```

## Parameters

- `patient`: A single patient to be updated. The patients must already exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyPatientStore Implementations
- [func updateAnyPatient(OCKAnyPatient, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyPatient>?)](./updateanypatient%28_,callbackqueue,completion%29-6ef0f.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatientstore/updateanypatient(_:callbackqueue:completion:))*