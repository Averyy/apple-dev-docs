---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarviewcontroller/init(store:viewsynchronizer:computeprogress:)"
framework: "CareKit/CareKit"
---

# init(store:viewSynchronizer:computeProgress:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Initialize a view controller that displays adherence. Fetches and stays synchronized with the adherence data.

## Declaration

```swift
@MainActor
init(store: OCKAnyStoreProtocol, viewSynchronizer: OCKWeekCalendarViewSynchronizer, computeProgress: @escaping (OCKAnyEvent) -> CareTaskProgress = { event in
            event.computeProgress(by: .checkingOutcomeExists)
        })
```

## Parameters

- `store`: Wraps the store that contains the adherence data.
- `viewSynchronizer`: Capable of creating and updating the view using the data series.
- `computeProgress`: Used to compute the progress for an event.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarviewcontroller/init(store:viewsynchronizer:computeprogress:))*