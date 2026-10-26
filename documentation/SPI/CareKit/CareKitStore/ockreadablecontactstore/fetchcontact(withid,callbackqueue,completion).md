---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecontactstore/fetchcontact(withid:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchContact(withID:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`fetchContact` asynchronously retrieves a contact from the store using its user-defined unique identifier. If a contact with the specified identifier is not found, the completion handler will be called with an error.

## Declaration

```swift
func fetchContact(withID id: String, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<Contact>)
```

## Parameters

- `id`: A unique user-defined identifier.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKReadableContactStore Implementations
- [func fetchContact(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<Contact>)](./fetchcontact%28withid,callbackqueue,completion%29-epk8.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecontactstore/fetchcontact(withid:callbackqueue:completion:))*