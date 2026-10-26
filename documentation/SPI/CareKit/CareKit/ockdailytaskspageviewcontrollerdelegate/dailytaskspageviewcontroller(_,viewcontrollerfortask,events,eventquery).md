---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockdailytaskspageviewcontrollerdelegate/dailytaskspageviewcontroller(_:viewcontrollerfortask:events:eventquery:)"
framework: "CareKit/CareKit"
---

# dailyTasksPageViewController(_:viewControllerForTask:events:eventQuery:)

**Framework**: CareKit/CareKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Return a view controller to display for the given task and events.

## Declaration

```swift
func dailyTasksPageViewController(_ viewController: OCKDailyTasksPageViewController, viewControllerForTask task: OCKAnyTask, events: [OCKAnyEvent], eventQuery: OCKEventQuery) -> UIViewController?
```

## Parameters

- `viewController`: The view controller displaying the returned view controller.
- `task`: The task to be displayed by the returned view controller.
- `events`: The events to be displayed by the returned view controller.
- `eventQuery`: The query used to retrieve the events for the task.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/ockdailytaskspageviewcontrollerdelegate/dailytaskspageviewcontroller(_:viewcontrollerfortask:events:eventquery:))*