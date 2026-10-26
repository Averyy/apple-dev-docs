---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/fetchcontact(withid:)"
framework: "CareKit/CareKitStore"
---

# fetchContact(withID:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

`fetchContact` asynchronously retrieves a contact from the store using its user-defined unique identifier. If a contact with the specified identifier is not found, the completion handler will be called with an error.

## Declaration

```swift
func fetchContact(withID id: String) async throws -> Contact
```

## Parameters

- `id`: The identifier of the item to be fetched.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/fetchcontact(withid:))*