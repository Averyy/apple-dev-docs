---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinatordelegate/outcomestore(_:shouldhandlewritingoutcome:)-3o51b"
framework: "CareKit/CareKitStore"
---

# outcomeStore(_:shouldHandleWritingOutcome:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Determines whether or not a store is intended to handle a certain write operation. The persistent store coordinator will call this method against all its stores in the order they were registered and execute the write on the first store that returns true for this method.

## Declaration

```swift
func outcomeStore(_ store: OCKAnyReadOnlyOutcomeStore, shouldHandleWritingOutcome outcome: OCKAnyOutcome) -> Bool
```

## Parameters

- `store`: A candidate store that should or should not handle writing.
- `outcome`: The outcome that needs to be written.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinatordelegate/outcomestore(_:shouldhandlewritingoutcome:)-3o51b)*