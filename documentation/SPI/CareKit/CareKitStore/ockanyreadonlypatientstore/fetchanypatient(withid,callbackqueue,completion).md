---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlypatientstore/fetchanypatient(withid:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchAnyPatient(withID:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`fetchAnyPatient` asynchronously retrieves a single patient from the store.

## Declaration

```swift
func fetchAnyPatient(withID id: String, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<OCKAnyPatient>)
```

## Parameters

- `id`: The identifier of the item to be fetched.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyReadOnlyPatientStore Implementations
- [func fetchAnyPatient(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyPatient>)](./fetchanypatient%28withid,callbackqueue,completion%29-611ga.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlypatientstore/fetchanypatient(withid:callbackqueue:completion:))*