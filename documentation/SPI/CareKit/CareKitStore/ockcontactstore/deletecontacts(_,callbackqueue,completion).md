---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactstore/deletecontacts(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteContacts(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`deleteContacts` asynchronously deletes an array of contacts from the store.

## Declaration

```swift
func deleteContacts(_ contacts: [Contact], callbackQueue: DispatchQueue, completion: OCKResultClosure<[Contact]>?)
```

## Parameters

- `contacts`: An array of contacts to be deleted. The contacts must exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactstore/deletecontacts(_:callbackqueue:completion:))*