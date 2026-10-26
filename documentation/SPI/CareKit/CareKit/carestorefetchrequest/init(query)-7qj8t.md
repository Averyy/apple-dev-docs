---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchrequest/init(query:)-7qj8t"
framework: "CareKit/CareKit"
---

# init(query:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Creates a fetch request for task data in a store that matches the provided query.

## Declaration

```swift
@MainActor
init(query: OCKTaskQuery)
```

Available when `Result` is `any OCKAnyTask` and `Query` is `OCKTaskQuery`.

#### Discussion

The result synchronizes with changes in the store.

## Parameters

- `query`: The query that matches data in the store during a fetch request.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchrequest/init(query:)-7qj8t)*