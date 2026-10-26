---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarviewcontroller/init(weekofdate:store:computeprogress:)"
framework: "CareKit/CareKit"
---

# init(weekOfDate:store:computeProgress:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Initialize a view controller that displays adherence. Fetches and stays synchronized with the adherence data.

## Declaration

```swift
@MainActor
init(weekOfDate date: Date, store: OCKAnyStoreProtocol, computeProgress: @escaping (OCKAnyEvent) -> CareTaskProgress = { event in
            event.computeProgress(by: .checkingOutcomeExists)
        })
```

## Parameters

- `date`: A date in the week for which adherence will be fetched.
- `store`: Contains the task data for which adherence will be computed.
- `computeProgress`: Used to compute the progress for an event.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockweekcalendarviewcontroller/init(weekofdate:store:computeprogress:))*