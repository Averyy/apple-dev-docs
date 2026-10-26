---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/synchronizedviewcontroller/init(initialviewmodel:viewmodels:viewsynchronizer:)"
framework: "CareKit/CareKit"
---

# init(initialViewModel:viewModels:viewSynchronizer:)

**Framework**: CareKit/CareKit  
**Kind**: init  
**Role**: Initializer

Creates a view controller that updates its view using a stream of data.

## Declaration

```swift
@MainActor
init<S>(initialViewModel: ViewSynchronizer.ViewModel, viewModels: S, viewSynchronizer: ViewSynchronizer) where S : AsyncSequence, ViewSynchronizer.ViewModel == S.Element
```

## Parameters

- `initialViewModel`: The initial value that appears in the view.
- `viewModels`: An asynchronous sequence of data that appears in the view.
- `viewSynchronizer`: The object that creates and updates the view.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/synchronizedviewcontroller/init(initialviewmodel:viewmodels:viewsynchronizer:))*