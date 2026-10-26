---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontactstore/addanycontacts(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addAnyContacts(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`addAnyContacts` asynchronously adds an array of contacts to the store.

## Declaration

```swift
func addAnyContacts(_ contacts: [OCKAnyContact], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyContact]>?)
```

## Parameters

- `contacts`: An array of contacts to be added to the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyContactStore Implementations
- [func addAnyContacts([OCKAnyContact], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyContact]>?)](./addanycontacts%28_,callbackqueue,completion%29-3dd59.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontactstore/addanycontacts(_:callbackqueue:completion:))*