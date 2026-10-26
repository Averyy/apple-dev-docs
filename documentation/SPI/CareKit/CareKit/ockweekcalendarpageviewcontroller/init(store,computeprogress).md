---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarpageviewcontroller/init(store:computeprogress:)"
framework: "CareKit/CareKit"
---

# init(store:computeProgress:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

A view controller that allows paging through adjacent weeks of task adherence content.

## Declaration

```swift
@MainActor
init(store: OCKAnyStoreProtocol, computeProgress: @escaping (OCKAnyEvent) -> CareTaskProgress = { event in
            event.computeProgress(by: .checkingOutcomeExists)
        })
```

## Parameters

- `store`: Contains the task data for which adherence will be computed.
- `computeProgress`: Used to compute the progress for an event.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarpageviewcontroller/init(store:computeprogress:))*