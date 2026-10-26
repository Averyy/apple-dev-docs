---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontactstore/deleteanycontacts(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteAnyContacts(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`deleteAnyContacts` asynchronously deletes an array of contacts from the store.

## Declaration

```swift
func deleteAnyContacts(_ contacts: [OCKAnyContact], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyContact]>?)
```

## Parameters

- `contacts`: An array of contacts to be deleted. The contacts must exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyContactStore Implementations
- [func deleteAnyContacts([OCKAnyContact], callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyContact]>?)](./deleteanycontacts%28_,callbackqueue,completion%29-3vmeg.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycontactstore/deleteanycontacts(_:callbackqueue:completion:))*