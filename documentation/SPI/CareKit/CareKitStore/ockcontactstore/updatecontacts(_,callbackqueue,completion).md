---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactstore/updatecontacts(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateContacts(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`updateContacts` asynchronously updates an array of contacts in the store.

## Declaration

```swift
func updateContacts(_ contacts: [Contact], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Contact]>?)
```

## Parameters

- `contacts`: An array of contacts to be updated. The contacts must already exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactstore/updatecontacts(_:callbackqueue:completion:))*