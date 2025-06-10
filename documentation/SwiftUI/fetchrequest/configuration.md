# FetchRequest.Configuration

**Framework**: SwiftUI  
**Kind**: struct

The request’s configurable properties.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@MainActor
@preconcurrency struct Configuration
```

#### Overview

You initialize a [`FetchRequest`](fetchrequest.md) with an optional predicate and sort descriptors, either explicitly or using a configured [`NSFetchRequest`](https://developer.apple.com/documentation/CoreData/NSFetchRequest). Later, you can dynamically update the predicate and sort parameters using the request’s configuration structure.

You access or bind to a request’s configuration components through properties on the associated [`FetchedResults`](fetchedresults.md) instance.

##### Configure Using a Binding

Get a [`Binding`](binding.md) to a fetch request’s configuration structure by accessing the request’s [`projectedValue`](fetchrequest/projectedvalue.md), which you do by using the dollar sign (`$`) prefix on the associated results property. For example, you can create a request for `Quake` entities — a managed object type that the [`Loading and Displaying a Large Data Feed`](loading_and_displaying_a_large_data_feed.md) sample code project defines — that initially sorts the results by time:

```swift
@FetchRequest(sortDescriptors: [SortDescriptor(\.time, order: .reverse)])
private var quakes: FetchedResults<Quake>
```

Then you can bind the request’s sort descriptors, which you access through the `quakes` result, to those of a [`Table`](table.md) instance:

```swift
Table(quakes, sortOrder: $quakes.sortDescriptors) {
    TableColumn("Place", value: \.place)
    TableColumn("Time", value: \.time) { quake in
        Text(quake.time, style: .time)
    }
}
```

A user who clicks on a table column header initiates the following sequence of events:

1. The table updates the sort descriptors through the binding.
2. The modified sort descriptors reconfigure the request.
3. The reconfigured request fetches new results.
4. SwiftUI redraws the table in response to new results.

##### Set Configuration Directly

If you need to access the fetch request’s configuration elements directly, use the [`nsPredicate`](fetchedresults/nspredicate.md) and [`sortDescriptors`](fetchedresults/sortdescriptors.md) or [`nsSortDescriptors`](fetchedresults/nssortdescriptors.md) properties of the [`FetchedResults`](fetchedresults.md) instance. Continuing the example above, to enable the user to dynamically update the predicate, declare a [`State`](state.md) property to hold a query string:

```swift
@State private var query = ""
```

Then add an [`onChange(of:initial:_:)`](view/onchange(of:initial:_:).md) modifier to the [`Table`](table.md) that sets a new predicate any time the query changes:

```swift
.onChange(of: query) { _, value in
    quakes.nsPredicate = query.isEmpty
        ? nil
        : NSPredicate(format: "place CONTAINS %@", value)
}
```

To give the user control over the string, add a [`TextField`](textfield.md) in your user interface that’s bound to the `query` state:

```swift
TextField("Filter", text: $query)
```

When the user types into the text field, the predicate updates, the request fetches new results, and SwiftUI redraws the table.

## Topics

### Setting a predicate
- [var nsPredicate: NSPredicate?](fetchrequest/configuration/nspredicate.md)
  The request’s predicate.
### Setting sort descriptors
- [var sortDescriptors: [SortDescriptor<Result>]](fetchrequest/configuration/sortdescriptors.md)
  The request’s sort descriptors, accessed as value types.
- [var nsSortDescriptors: [NSSortDescriptor]](fetchrequest/configuration/nssortdescriptors.md)
  The request’s sort descriptors, accessed as reference types.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var projectedValue: Binding<FetchRequest<Result>.Configuration>](fetchrequest/projectedvalue.md)
  A binding to the request’s mutable configuration properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/fetchrequest/configuration)*