# init(_:description:)

**Framework**: Evaluations  
**Kind**: init  
**Role**: Initializer

Creates a metric with a name and an optional description.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
init(_ name: String, description: String? = nil)
```

## Discussion

```swift
let metric = Metric("Accuracy", description: "Share of answers that matched.")
```

Use the factory methods — `passing`, `failing`, `scoring`, or `ignore` — to produce results.

## Parameters

- `name`: The name of the metric.
- `description`: What the metric measures, in inline Markdown. `nil` for none.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric/init(_:description:))*