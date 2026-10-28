---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/attach(planstore:)"
framework: "CareKit/CareKitStore"
---

# attach(planStore:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Attaches a new store. The new store must be capable of reading and writing care plans.

## Declaration

```swift
func attach(planStore: OCKAnyCarePlanStore)
```

## Discussion

> **Note**: The order is which stores are attached is important.

> **See Also**: `OCKStoreCoordinator`

## Parameters

- `planStore`: Any store that conforms to `OCKAnyCarePlanStore`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/attach(planstore:))*