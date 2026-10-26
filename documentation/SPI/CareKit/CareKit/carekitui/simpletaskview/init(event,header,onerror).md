---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carekitui/simpletaskview/init(event:header:onerror:)"
framework: "CareKit/CareKit"
---

# init(event:header:onError:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Create a view using data from an event.

## Declaration

```swift
@MainActor
init(event: CareStoreFetchedResult<OCKAnyEvent>, @ViewBuilder header: () -> Header, onError: @escaping (OCKStoreError) -> Void = { _ in })
```

Available when `Header` conforms to `View`.

#### Discussion

This view displays a button to toggle completion for the event.

## Parameters

- `event`: The data be displayed in the view.
- `header`: Short and descriptive content that identifies the event.
- `onError`: A closure that the struct calls if an error occurs while toggling completion for the event.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carekitui/simpletaskview/init(event:header:onerror:))*