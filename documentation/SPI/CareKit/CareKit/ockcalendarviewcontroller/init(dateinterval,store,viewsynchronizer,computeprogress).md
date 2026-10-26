---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcalendarviewcontroller/init(dateinterval:store:viewsynchronizer:computeprogress:)"
framework: "CareKit/CareKit"
---

# init(dateInterval:store:viewSynchronizer:computeProgress:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Initialize a view controller that displays adherence per date. Fetches and stays synchronized with the adherence data.

## Declaration

```swift
@MainActor
init(dateInterval: DateInterval, store: OCKAnyStoreProtocol, viewSynchronizer: ViewSynchronizer, computeProgress: @escaping (OCKAnyEvent) -> CareTaskProgress = { event in
            event.computeProgress(by: .checkingOutcomeExists)
        })
```

## Parameters

- `dateInterval`: A date interval for which adherence will be displayed.
- `store`: Contains the task data for which adherence will be computed.
- `viewSynchronizer`: Capable of creating and updating the view.
- `computeProgress`: Used to compute the progress for an event.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockcalendarviewcontroller/init(dateinterval:store:viewsynchronizer:computeprogress:))*