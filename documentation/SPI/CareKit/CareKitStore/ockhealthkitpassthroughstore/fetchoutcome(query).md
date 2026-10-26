---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkitpassthroughstore/fetchoutcome(query:)"
framework: "CareKit/CareKitStore"
---

# fetchOutcome(query:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

`fetchOutcome` asynchronously retrieves a single outcome from the store. If more than one outcome matches the query, only the first will be returned. If no matching outcomes exist, the completion handler will be called with an error.

## Declaration

```swift
func fetchOutcome(query: OCKOutcomeQuery) async throws -> Outcome
```

## Parameters

- `query`: A query used to constrain the values that will be fetched.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockhealthkitpassthroughstore/fetchoutcome(query:))*