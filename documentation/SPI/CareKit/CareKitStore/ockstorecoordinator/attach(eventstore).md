---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/attach(eventstore:)"
framework: "CareKit/CareKitStore"
---

# attach(eventStore:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Attaches a new store. The new store must be capable of reading and writing tasks and outcomes.

## Declaration

```swift
func attach(eventStore: OCKAnyEventStore)
```

## Discussion

> **Note**: The order is which stores are attached is important.

> **See Also**: `OCKStoreCoordinator`

## Parameters

- `eventStore`: Any store that conforms to `OCKAnyEventStore`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/attach(eventstore:))*