---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinatordelegate/careplanstore(_:shouldhandlewritingcareplan:)"
framework: "CareKit/CareKitStore"
---

# carePlanStore(_:shouldHandleWritingCarePlan:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Determines whether or not a store is intended to handle a certain write operation. The persistent store coordinator will call this method against all its stores in the order they were registered and execute the write on the first store that returns true for this method.

## Declaration

```swift
func carePlanStore(_ store: OCKAnyCarePlanStore, shouldHandleWritingCarePlan plan: OCKAnyCarePlan) -> Bool
```

## Parameters

- `store`: A candidate store that should or should not handle writing.
- `plan`: The plan that needs to be written.

## Default Implementations

### OCKStoreCoordinatorDelegate Implementations
- [func carePlanStore(OCKAnyCarePlanStore, shouldHandleWritingCarePlan: OCKAnyCarePlan) -> Bool](./careplanstore%28_,shouldhandlewritingcareplan%29-1ftoz.md)
  Determines whether or not a store is intended to handle a certain write operation. The persistent store coordinator will call this method against all its stores in the order they were registered and execute the write on the first store that returns true for this method.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinatordelegate/careplanstore(_:shouldhandlewritingcareplan:))*