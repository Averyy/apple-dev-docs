---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactstore/addcontacts(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addContacts(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`addContacts` asynchronously adds an array of contacts to the store.

## Declaration

```swift
func addContacts(_ contacts: [Contact], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Contact]>?)
```

## Parameters

- `contacts`: An array of contacts to be added to the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactstore/addcontacts(_:callbackqueue:completion:))*