---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchrequest/init(query:)-7io2h"
framework: "CareKit/CareKit"
---

# init(query:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Creates a fetch request for event data in a store that matches the provided query.

## Declaration

```swift
@MainActor
init(query: OCKEventQuery)
```

Available when `Result` is `OCKAnyEvent` and `Query` is `OCKEventQuery`.

#### Discussion

The result synchronizes with changes in the store.

## Parameters

- `query`: The query that matches data in the store during a fetch request.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchrequest/init(query:)-7io2h)*