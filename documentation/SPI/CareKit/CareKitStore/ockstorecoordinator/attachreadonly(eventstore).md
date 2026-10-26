---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/attachreadonly(eventstore:)"
framework: "CareKit/CareKitStore"
---

# attachReadOnly(eventStore:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Attaches a new store. The new store must be capable of reading events.

## Declaration

```swift
func attachReadOnly(eventStore: OCKAnyReadOnlyEventStore)
```

#### Discussion

> **Note**: The order is which stores are attached is important.

> **See Also**: `OCKStoreCoordinator`

## Parameters

- `eventStore`: Any store that conforms to `OCKAnyReadOnlyEventStore`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/attachreadonly(eventstore:))*