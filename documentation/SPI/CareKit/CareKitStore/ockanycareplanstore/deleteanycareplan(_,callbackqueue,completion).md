---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycareplanstore/deleteanycareplan(_:callbackqueue:completion:)"
framework: "CareKit/CareKitStore"
---

# deleteAnyCarePlan(_:callbackQueue:completion:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Asynchronously deletes a single care plan from the store.

## Declaration

```swift
func deleteAnyCarePlan(_ plan: OCKAnyCarePlan, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyCarePlan>?)
```

## Parameters

- `plan`: A single care plan to delete. The care plans must exist in the store.
- `callbackQueue`: The queue that the method calls the completion closure on. In most cases this is the main queue.
- `completion`: A callback that executes on the provided callback queue.

## Default Implementations

### OCKAnyCarePlanStore Implementations
- [func deleteAnyCarePlan(OCKAnyCarePlan, callbackQueue: DispatchQueue, completion: OCKResultClosure<OCKAnyCarePlan>?)](./deleteanycareplan%28_,callbackqueue,completion%29-6zdn1.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockanycareplanstore/deleteanycareplan(_:callbackqueue:completion:))*