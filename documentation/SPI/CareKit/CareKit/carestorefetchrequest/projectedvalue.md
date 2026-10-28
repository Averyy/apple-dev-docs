---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchrequest/projectedvalue"
framework: "CareKit/CareKit"
---

# projectedValue

**Framework**: CareKit/CareKit  
**Kind**: property  
**Role**: Instance Property

A binding to the parameters you use to fetch data from a CareKit store.

## Declaration

```swift
@MainActor
var projectedValue: Binding<Configuration> { get }
```

## Discussion

Modifying the parameters executes a new fetch request.

Here’s an example for fetching tasks from a store:

```swift
    @CareStoreFetchRequest(query: OCKTaskQuery())
    private var tasks
```

You can change the configuration dynamically:

```swift
    Button("Update Query") {
        tasks.query = newQuery
    }
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekit/carestorefetchrequest/projectedvalue)*