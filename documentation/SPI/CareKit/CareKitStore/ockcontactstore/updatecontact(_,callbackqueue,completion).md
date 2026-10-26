---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactstore/updatecontact(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# updateContact(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`updateContact` asynchronously updates a contacts in the store.

## Declaration

```swift
func updateContact(_ contact: Contact, callbackQueue: DispatchQueue, completion: OCKResultClosure<Contact>?)
```

## Parameters

- `contact`: A contact to be updated. The contact must already exist in the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKContactStore Implementations
- [func updateContact(Contact, callbackQueue: DispatchQueue, completion: OCKResultClosure<Contact>?)](./updatecontact%28_,callbackqueue,completion%29-4ye33.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactstore/updatecontact(_:callbackqueue:completion:))*