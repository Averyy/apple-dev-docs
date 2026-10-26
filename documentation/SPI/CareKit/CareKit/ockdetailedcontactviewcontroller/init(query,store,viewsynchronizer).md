---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockdetailedcontactviewcontroller/init(query:store:viewsynchronizer:)"
framework: "CareKit/CareKit"
---

# init(query:store:viewSynchronizer:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

A view controller that displays a contact view and keeps it synchronized with a store.

## Declaration

```swift
@MainActor
override init(query: OCKContactQuery, store: OCKAnyStoreProtocol, viewSynchronizer: OCKDetailedContactViewSynchronizer = OCKDetailedContactViewSynchronizer())
```

## Parameters

- `query`: Used to fetch the contact data that will be displayed.
- `store`: Contains the contact data that will be displayed.
- `viewSynchronizer`: Capable of creating and updating the view using the contact data.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockdetailedcontactviewcontroller/init(query:store:viewsynchronizer:))*