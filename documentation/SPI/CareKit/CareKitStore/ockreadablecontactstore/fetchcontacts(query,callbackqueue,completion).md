---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecontactstore/fetchcontacts(query:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# fetchContacts(query:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

`fetchContacts` asynchronously retrieves an array of contacts from the store.

## Declaration

```swift
func fetchContacts(query: OCKContactQuery, callbackQueue: DispatchQueue, completion: @escaping OCKResultClosure<[Contact]>)
```

## Parameters

- `query`: A query used to constrain the values that will be fetched.
- `callbackQueue`: The queue that the completion closure should be called on. In most cases this should be the main queue.
- `completion`: A callback that will fire on the provided callback queue.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecontactstore/fetchcontacts(query:callbackqueue:completion:))*