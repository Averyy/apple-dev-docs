---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchrequest"
framework: "CareKit/CareKit"
---

# CareStoreFetchRequest

**Framework**: CareKit/CareKit  
**Kind**: struct  
**Role**: Structure

A property wrapper useful for streaming data from a CareKit store.

## Declaration

```swift
@propertyWrapper
@MainActor struct CareStoreFetchRequest<Result, Query>
```

## Overview

The property wrapper offers a few initializers matching the different entities available in the CareKit store. Each initializer requires a query that is used to locate the desired data.

```swift
    @CareStoreFetchRequest(query: OCKTaskQuery())
    private var tasks
```

CareKit stores the fetched results in the `wrappedValue` and stays up to date with changes to the store.

The property wrapper also offers a binding to the query in case you need to modify it. Modifying the query initiates a new fetch request.

```swift
    Button("Update Query") {
        tasks.query = newQuery
    }
```

Define the property wrapper on a `View` that contains the store in its environment. You can inject the store through the environment like this:

```swift
    ContentView()
        .environment(\.careStore, store)
```

See the `OCKAnyStoreProtocol` and the `OCKStore` for more information about creating a CareKit store.

You may need to update the query over time. For example, you’re using the property wrapper to fetch and display tasks for `today`. After midnight passes, `today` changes, so you need to fetch new results. To detect events such as the passage of a day or a change of time zone, observe [significantTimeChangeNotification](https://developer.apple.com/documentation/uikit/uiapplication/1623059-significanttimechangenotificatio).

```swift
    ContentView()
        .onReceive(NotificationCenter.default.publisher(for: UIApplication.significantTimeChangeNotification)) { _ in
            tasks.query.dateInterval = Calendar.current.dateInterval(of: .day, for: Date())!
    }
```

If you prefer to update the query date at a very specific time interval, see https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/swiftui/timelineview.

## Topics

### Structures
- [CareStoreFetchRequest.Configuration](./carestorefetchrequest/configuration.md)
  A structure that contains query information you use to stream data from a CareKit store.
### Initializers
- [init(query: OCKOutcomeQuery)](./carestorefetchrequest/init%28query%29-76xs7.md)
  Creates a fetch request for outcome data in a store that matches the provided query.
- [init(query: OCKEventQuery)](./carestorefetchrequest/init%28query%29-7io2h.md)
  Creates a fetch request for event data in a store that matches the provided query.
- [init(query: OCKCarePlanQuery)](./carestorefetchrequest/init%28query%29-7mrlf.md)
  Creates a fetch request for care plan data in a store that matches the provided query.
- [init(query: OCKTaskQuery)](./carestorefetchrequest/init%28query%29-7qj8t.md)
  Creates a fetch request for task data in a store that matches the provided query.
- [init(query: OCKContactQuery)](./carestorefetchrequest/init%28query%29-8izl2.md)
  Creates a fetch request for contact data in a store that matches the provided query.
- [init(query: OCKPatientQuery)](./carestorefetchrequest/init%28query%29-ggiz.md)
  Creates a fetch request for patient data in a store that matches the provided query.
### Instance Properties
- [var projectedValue: Binding<Configuration>](./carestorefetchrequest/projectedvalue.md)
  A binding to the parameters you use to fetch data from a CareKit store.
- [var wrappedValue: CareStoreFetchedResults<Result, Query>](./carestorefetchrequest/wrappedvalue.md)
  The result fetched from the CareKit store.
### Instance Methods
- [func update()](./carestorefetchrequest/update%28%29.md)

## Relationships

### Conforms To
- Swift.Sendable
- SwiftUICore.DynamicProperty

## See Also

### Displaying synchronized care data in SwiftUI
- [struct CareStoreFetchedResults](./carestorefetchedresults.md)
  A batch of results fetched from the store.
- [struct CareStoreFetchedResult](./carestorefetchedresult.md)
  A result fetched from the store.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchrequest)*