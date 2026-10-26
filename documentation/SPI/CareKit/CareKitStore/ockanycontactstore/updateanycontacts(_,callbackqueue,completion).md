---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontactstore/updateanycontacts(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateAnyContacts(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`updateAnyContacts` asynchronously updates an array of contacts in the store.

## Declaration

```swift
func updateAnyContacts(_ contacts: [OCKAnyContact], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyContact]>?)
```

## Parameters

- `contacts`: An array of contacts to be updated. The contacts must already exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyContactStore Implementations
- [func updateAnyContacts([OCKAnyContact], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyContact]>?)](./updateanycontacts%28_,callbackqueue,completion%29-9apu4.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontactstore/updateanycontacts(_:callbackqueue:completion:))*