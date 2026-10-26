---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontactstore/deleteanycontact(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteAnyContact(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`deleteAnyContact` asynchronously deletes a single contact from the store.

## Declaration

```swift
func deleteAnyContact(_ contact: OCKAnyContact, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyContact>?)
```

## Parameters

- `contact`: A single contact to be deleted. The contact must exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyContactStore Implementations
- [func deleteAnyContact(OCKAnyContact, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyContact>?)](./deleteanycontact%28_,callbackqueue,completion%29-59eep.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontactstore/deleteanycontact(_:callbackqueue:completion:))*