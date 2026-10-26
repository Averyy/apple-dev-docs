---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycontactstore/fetchanycontact(withid:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchAnyContact(withID:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`fetchAnyContact` asynchronously retrieves a single contact from the store.

## Declaration

```swift
func fetchAnyContact(withID id: String, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<OCKAnyContact>)
```

## Parameters

- `id`: The identifier of the item to be fetched.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyReadOnlyContactStore Implementations
- [func fetchAnyContact(withID: String, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyContact>)](./fetchanycontact%28withid,callbackqueue,completion%29-53y48.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycontactstore/fetchanycontact(withid:callbackqueue:completion:))*