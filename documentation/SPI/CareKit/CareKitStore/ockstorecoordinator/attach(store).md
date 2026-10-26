---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/attach(store:)"
framework: "CareKit/CareKitStore"
---

# attach(store:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Attaches a new store. The new store must be capable of handling reading and writing to all object types.

## Declaration

```swift
func attach(store: OCKAnyStoreProtocol)
```

#### Discussion

> **Note**: The order is which stores are attached is important.

> **See Also**: `OCKStoreCoordinator`

## Parameters

- `store`: Any store that conforms to `OCKAnyStoreProtocol`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/attach(store:))*