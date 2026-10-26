---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchrequest/init(query:)-7mrlf"
framework: "CareKit/CareKit"
---

# init(query:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Creates a fetch request for care plan data in a store that matches the provided query.

## Declaration

```swift
@MainActor
init(query: OCKCarePlanQuery)
```

Available when `Result` is `any OCKAnyCarePlan` and `Query` is `OCKCarePlanQuery`.

#### Discussion

The result synchronizes with changes in the store.

## Parameters

- `query`: The query that matches data in the store during a fetch request.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchrequest/init(query:)-7mrlf)*