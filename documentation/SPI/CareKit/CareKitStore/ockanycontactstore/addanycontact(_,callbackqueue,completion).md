---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontactstore/addanycontact(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addAnyContact(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`addAnyContact` asynchronously adds a single contact to the store.

## Declaration

```swift
func addAnyContact(_ contact: OCKAnyContact, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyContact>?)
```

## Parameters

- `contact`: A single contact to be added to the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyContactStore Implementations
- [func addAnyContact(OCKAnyContact, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyContact>?)](./addanycontact%28_,callbackqueue,completion%29-6qn3g.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontactstore/addanycontact(_:callbackqueue:completion:))*