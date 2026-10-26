---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/fetchanyoutcome(query:)"
framework: "CareKit/CareKitStore"
---

# fetchAnyOutcome(query:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Asynchronously retrieve a single outcome from the store.

## Declaration

```swift
func fetchAnyOutcome(query: OCKOutcomeQuery) async throws -> OCKAnyOutcome
```

#### Discussion

If more than one outcome matches the query, only the first returns. If no matching outcomes exist, the completion handler receives an error.

## Parameters

- `query`: A query that constrains the fetched values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstore/fetchanyoutcome(query:))*