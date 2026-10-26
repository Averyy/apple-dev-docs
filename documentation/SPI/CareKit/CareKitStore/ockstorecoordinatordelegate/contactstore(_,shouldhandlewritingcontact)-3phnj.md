---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinatordelegate/contactstore(_:shouldhandlewritingcontact:)-3phnj"
framework: "CareKit/CareKitStore"
---

# contactStore(_:shouldHandleWritingContact:)

**Framework**: CareKit/CareKitStore  
**Kind**: method  
**Role**: Instance Method

Determines whether or not a store is intended to handle a certain write operation. The persistent store coordinator will call this method against all its stores in the order they were registered and execute the write on the first store that returns true for this method.

## Declaration

```swift
func contactStore(_ store: OCKAnyReadOnlyContactStore, shouldHandleWritingContact contact: OCKAnyContact) -> Bool
```

## Parameters

- `store`: A candidate store that should or should not handle writing.
- `contact`: The contact that needs to be written.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitstore/ockstorecoordinatordelegate/contactstore(_:shouldhandlewritingcontact:)-3phnj)*