# Executing Activity Summary Queries

**Framework**: HealthKit

Create and run activity summary queries.

#### Overview

Use activity summary queries to read [`HKActivitySummary`](hkactivitysummary.md) objects from the HealthKit store. Apps can display summary information using an activity ring view ([`HKActivityRingView`](https://developer.apple.com/documentation/healthkitui/hkactivityringview) on iOS or [`WKInterfaceActivityRing`](https://developer.apple.com/documentation/WatchKit/WKInterfaceActivityRing) on watchOS).

##### Create the Predicate

Start by creating a predicate for summaries over the previous week.

```swift
let calendar = NSCalendar.current
let endDate = Date()
 
guard let startDate = calendar.date(byAdding: .day, value: -7, to: endDate) else {
    fatalError("*** Unable to create the start date ***")
}

let units: Set<Calendar.Component> = [.day, .month, .year, .era]

var startDateComponents = calendar.dateComponents(units, from: startDate)
startDateComponents.calendar = calendar

var endDateComponents = calendar.dateComponents(units, from: endDate)
endDateComponents.calendar = calendar

// Create the predicate for the query
let summariesWithinRange = HKQuery.predicate(forActivitySummariesBetweenStart: startDateComponents,
                                             end: endDateComponents)
```

##### Create the Query

Then create an activity summary query by calling the [`init(predicate:resultsHandler:)`](hkactivitysummaryquery/init(predicate:resultshandler:).md) initializer.

```swift
let query = HKActivitySummaryQuery(predicate: summariesWithinRange) { (query, summariesOrNil, errorOrNil) -> Void in
    
    guard let summaries = summariesOrNil else {
        // Handle any errors here.
        return
    }
    
    for summary in summaries {
        // Process each summary here.
    }
    
    // The results come back on an anonymous background queue.
    // Dispatch to the main queue before modifying the UI.
    
    DispatchQueue.main.async {
        // Update the UI here.
    }
}
```

The query returns an array of activity summary objects. The results handler should check for errors before processing the summaries. It should also dispatch updates to the user interface back to the main thread.

##### Run the Query

After instantiating the query, call the HealthKit store’s [`execute(_:)`](hkhealthstore/execute(_:).md) method.

```swift
store.execute(query)
```

This method runs the query on an anonymous background queue. When the query is complete, it executes the results handler on the same background queue (but not necessarily on the same thread).

## See Also

- [init(predicate: NSPredicate?, resultsHandler: (HKActivitySummaryQuery, [HKActivitySummary]?, (any Error)?) -> Void)](hkactivitysummaryquery/init(predicate:resultshandler:).md)
  Initializes a new active summary query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/executing-activity-summary-queries)*