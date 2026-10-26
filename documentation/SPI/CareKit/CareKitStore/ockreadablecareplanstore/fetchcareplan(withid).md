---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecareplanstore/fetchcareplan(withid:)"
framework: "CareKit/CareKitStore"
---

# fetchCarePlan(withID:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

`fetchCarePlan` asynchronously retrieves a care plan from the store using its user-defined unique identifier. If a care plan with the specified identifier is not found, the completion handler will be called with an error.

## Declaration

```swift
func fetchCarePlan(withID id: String) async throws -> Plan
```

## Parameters

- `id`: The identifier of the item to be fetched.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockreadablecareplanstore/fetchcareplan(withid:))*