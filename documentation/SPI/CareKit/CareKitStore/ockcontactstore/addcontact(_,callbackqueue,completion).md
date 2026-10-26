---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactstore/addcontact(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# addContact(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`addContact` asynchronously adds a contact to the store.

## Declaration

```swift
func addContact(_ contact: Contact, callbackQueue: DispatchQueue, completion: OCKResultClosure<Contact>?)
```

## Parameters

- `contact`: A contact to be added to the store.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKContactStore Implementations
- [func addContact(Contact, callbackQueue: DispatchQueue, completion: OCKResultClosure<Contact>?)](./addcontact%28_,callbackqueue,completion%29-9vyyd.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockcontactstore/addcontact(_:callbackqueue:completion:))*