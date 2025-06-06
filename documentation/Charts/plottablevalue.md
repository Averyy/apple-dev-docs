# PlottableValue

**Framework**: Swift Charts  
**Kind**: struct

Labeled data that you plot in a chart using marks.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct PlottableValue<Value> where Value : Plottable
```

#### Overview

Provide a `PlottableValue` to a `Mark` property (e.g., x, y, foregroundStyle) to plot data values with the mark property.

> ❗ **Important**: The data type must conform to [`Plottable`](plottable.md). This is a numeric value like a [`Double`](https://developer.apple.com/documentation/Swift/Double) or [`Int16`](https://developer.apple.com/documentation/Swift/Int16) for quantitative data, [`Date`](https://developer.apple.com/documentation/Foundation/Date) for temporal data, or [`String`](https://developer.apple.com/documentation/Swift/String) for categorical data.

The data type must conform to [`Plottable`](plottable.md). This is a numeric value like a [`Double`](https://developer.apple.com/documentation/Swift/Double) or [`Int16`](https://developer.apple.com/documentation/Swift/Int16) for quantitative data, [`Date`](https://developer.apple.com/documentation/Foundation/Date) for temporal data, or [`String`](https://developer.apple.com/documentation/Swift/String) for categorical data.

You can use the `.value("Category", \.category)` shorthand to create a `PlottableValue`. The example below plots category, value, and group with the bar mark’s x, y, and foregroundStyle.

```swift
struct Bar {
    let category: String
    let value: Double
    let group: String
}

let data: [Bar] = [
    Bar(category: "A", value: 20, group: "Group 1"),
    Bar(category: "A", value: 30, group: "Group 2"),
    Bar(category: "A", value: 10, group: "Group 3"),
    Bar(category: "B", value: 40, group: "Group 1"),
    Bar(category: "B", value: 20, group: "Group 2"),
    Bar(category: "B", value: 10, group: "Group 3"),
    //...
]

var body: some View {
    Chart(data) {
        BarMark(
            x: .value("Category", $0.category),
            y: .value("Quantity", $0.value)
        )
        .foregroundStyle(.value("Group", $0.group))
    }
}
```

## Topics

### Type Methods
- [static func value<S>(S, Value) -> PlottableValue<Value>](plottablevalue/value(_:_:)-13lvv.md)
  Creates a parameter value with label and value.
- [static func value(LocalizedStringKey, Range<Value>) -> PlottableValue<Value>](plottablevalue/value(_:_:)-3sze5.md)
  Creates a parameter value with label key and value.
- [static func value(Text, Range<Value>) -> PlottableValue<Value>](plottablevalue/value(_:_:)-4qa4d.md)
  Creates a parameter value with label and value.
- [static func value<S>(S, ChartBinRange<Value>) -> PlottableValue<Value>](plottablevalue/value(_:_:)-6jxfn.md)
  Creates a parameter value with label and value.
- [static func value(LocalizedStringKey, Value) -> PlottableValue<Value>](plottablevalue/value(_:_:)-70xhu.md)
  Creates a parameter value with label key and value.
- [static func value(Text, Value) -> PlottableValue<Value>](plottablevalue/value(_:_:)-7ed58.md)
  Creates a parameter value with label and value.
- [static func value(LocalizedStringKey, ChartBinRange<Value>) -> PlottableValue<Value>](plottablevalue/value(_:_:)-7k0m0.md)
  Creates a parameter value with label key and value.
- [static func value(Text, ChartBinRange<Value>) -> PlottableValue<Value>](plottablevalue/value(_:_:)-9bdsw.md)
  Creates a parameter value with label and value.
- [static func value<S>(S, Range<Value>) -> PlottableValue<Value>](plottablevalue/value(_:_:)-f1kk.md)
  Creates a parameter value with label and value.
- [static func value<S>(S, Date, unit: Calendar.Component, calendar: Calendar?) -> PlottableValue<Value>](plottablevalue/value(_:_:unit:calendar:)-2r0fo.md)
  Creates a parameter value with label and value.
- [static func value(LocalizedStringKey, Date, unit: Calendar.Component, calendar: Calendar?) -> PlottableValue<Value>](plottablevalue/value(_:_:unit:calendar:)-8f7fe.md)
  Creates a parameter value with label key and value.
- [static func value(Text, Date, unit: Calendar.Component, calendar: Calendar?) -> PlottableValue<Value>](plottablevalue/value(_:_:unit:calendar:)-liyc.md)
  Creates a parameter value with label and value.

## See Also

- [protocol Plottable](plottable.md)
  A type that can serve as data to plot in a chart.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/plottablevalue)*