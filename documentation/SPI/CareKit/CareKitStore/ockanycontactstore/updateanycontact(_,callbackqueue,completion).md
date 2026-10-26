---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontactstore/updateanycontact(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateAnyContact(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`updateAnyContact` asynchronously update single contact in the store.

## Declaration

```swift
func updateAnyContact(_ contact: OCKAnyContact, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyContact>?)
```

## Parameters

- `contact`: A single contact to be updated. The contact must already exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyContactStore Implementations
- [func updateAnyContact(OCKAnyContact, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyContact>?)](./updateanycontact%28_,callbackqueue,completion%29-1f4tu.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontactstore/updateanycontact(_:callbackqueue:completion:))*