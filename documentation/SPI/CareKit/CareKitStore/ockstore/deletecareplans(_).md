---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/deletecareplans(_:)"
framework: "CareKit/CareKitStore"
---

# deleteCarePlans(_:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

`deleteCarePlans` asynchronously deletes an array of care plans from the store.

## Declaration

```swift
@discardableResult
func deleteCarePlans(_ plans: [Plan]) async throws -> [Plan]
```

## Parameters

- `plans`: An array of care plans to be deleted. The care plans must exist in the store.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/deletecareplans(_:))*