---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactstore/deletecontact(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteContact(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`deleteContact` asynchronously deletes a contact from the store.

## Declaration

```swift
func deleteContact(_ contact: Contact, callbackQueue: DispatchQueue, completion: OCKResultClosure<Contact>?)
```

## Parameters

- `contact`: A contact to be deleted. The contact must exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKContactStore Implementations
- [func deleteContact(Contact, callbackQueue: DispatchQueue, completion: OCKResultClosure<Contact>?)](./deletecontact%28_,callbackqueue,completion%29-3nnq7.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactstore/deletecontact(_:callbackqueue:completion:))*