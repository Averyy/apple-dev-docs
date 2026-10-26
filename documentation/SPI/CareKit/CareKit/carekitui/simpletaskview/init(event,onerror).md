---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carekitui/simpletaskview/init(event:onerror:)"
framework: "CareKit/CareKit"
---

# init(event:onError:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Create a view using data from an event.

## Declaration

```swift
@MainActor
init(event: CareStoreFetchedResult<OCKAnyEvent>, onError: @escaping (OCKStoreError) -> Void = { _ in })
```

Available when `Header` is `_SimpleTaskViewHeader`.

#### Discussion

This view displays a button to toggle completion for the event.

## Parameters

- `event`: The data displayed in the view.
- `onError`: A closure that the struct calls if an error occurs while toggling completion for the event.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carekitui/simpletaskview/init(event:onerror:))*