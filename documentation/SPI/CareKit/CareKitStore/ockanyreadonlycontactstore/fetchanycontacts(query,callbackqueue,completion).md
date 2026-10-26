---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycontactstore/fetchanycontacts(query:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchAnyContacts(query:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`fetchAnyContacts` asynchronously retrieves an array of contacts from the store.

## Declaration

```swift
func fetchAnyContacts(query: OCKContactQuery, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<[OCKAnyContact]>)
```

## Parameters

- `query`: A query used to constrain the values that will be fetched.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.

## Default Implementations

### OCKAnyReadOnlyContactStore Implementations
- [func fetchAnyContacts(query: OCKContactQuery, callbackQueue: DispatchQueue, completion: OCKResultClosure<[OCKAnyContact]>)](./fetchanycontacts%28query,callbackqueue,completion%29-97xek.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanyreadonlycontactstore/fetchanycontacts(query:callbackqueue:completion:))*