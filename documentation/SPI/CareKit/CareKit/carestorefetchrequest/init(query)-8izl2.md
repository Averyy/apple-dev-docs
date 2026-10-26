---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchrequest/init(query:)-8izl2"
framework: "CareKit/CareKit"
---

# init(query:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Creates a fetch request for contact data in a store that matches the provided query.

## Declaration

```swift
@MainActor
init(query: OCKContactQuery)
```

Available when `Result` is `any OCKAnyContact` and `Query` is `OCKContactQuery`.

#### Discussion

The result synchronizes with changes in the store.

## Parameters

- `query`: The query that matches data in the store during a fetch request.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchrequest/init(query:)-8izl2)*