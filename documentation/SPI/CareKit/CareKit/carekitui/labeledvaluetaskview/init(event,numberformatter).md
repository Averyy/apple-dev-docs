---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carekitui/labeledvaluetaskview/init(event:numberformatter:)"
framework: "CareKit/CareKit"
---

# init(event:numberFormatter:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Create a view using data from an event.

## Declaration

```swift
@MainActor
init(event: CareStoreFetchedResult<OCKAnyEvent>, numberFormatter: NumberFormatter? = nil)
```

Available when `Header` is `_LabeledValueTaskViewHeader`.

#### Discussion

This view displays the numeric progress for the event by summing outcome values.

## Parameters

- `event`: The data that appears in the view.
- `numberFormatter`: An object that formats the progress and target values.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carekitui/labeledvaluetaskview/init(event:numberformatter:))*