# init(_:)

**Framework**: Evaluations  
**Kind**: init

Creates a metric with just a name.

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
init(_ name: String)
```

#### Discussion

```swift
let metric = Metric("Accuracy")
```

Use the factory methods — `passing`, `failing`, `scoring`, or `ignore` — to produce results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/metric/init(_:))*