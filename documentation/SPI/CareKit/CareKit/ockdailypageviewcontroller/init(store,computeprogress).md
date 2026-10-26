---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockdailypageviewcontroller/init(store:computeprogress:)"
framework: "CareKit/CareKit"
---

# init(store:computeProgress:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Create an instance of the view controller. Will hook up the calendar to the tasks collection, and query and display the tasks.

## Declaration

```swift
@MainActor
init(store: OCKAnyStoreProtocol, computeProgress: @escaping (OCKAnyEvent) -> CareTaskProgress = { event in
            event.computeProgress(by: .checkingOutcomeExists)
        })
```

## Parameters

- `store`: The store from which to query the tasks.
- `computeProgress`: Used to compute the combined progress for a series of CareKit events.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockdailypageviewcontroller/init(store:computeprogress:))*