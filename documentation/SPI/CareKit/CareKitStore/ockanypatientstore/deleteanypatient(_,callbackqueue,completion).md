---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatientstore/deleteanypatient(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteAnyPatient(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`deleteAnyPatient` asynchronously deletes a single patient from the store.

## Declaration

```swift
func deleteAnyPatient(_ patient: OCKAnyPatient, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyPatient>?)
```

## Parameters

- `patient`: A single patient to be deleted. The patients must exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyPatientStore Implementations
- [func deleteAnyPatient(OCKAnyPatient, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyPatient>?)](./deleteanypatient%28_,callbackqueue,completion%29-9larp.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanypatientstore/deleteanypatient(_:callbackqueue:completion:))*