---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/attachreadonly(careplanstore:)"
framework: "CareKit/CareKitStore"
---

# attachReadOnly(carePlanStore:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Attaches a new store. The new store must be capable of reading care plans.

## Declaration

```swift
func attachReadOnly(carePlanStore: OCKAnyReadOnlyCarePlanStore)
```

#### Discussion

> **Note**: The order is which stores are attached is important.

> **See Also**: `OCKStoreCoordinator`

## Parameters

- `carePlanStore`: Any store that conforms to `OCKAnyReadOnlyCarePlanStore`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinator/attachreadonly(careplanstore:))*