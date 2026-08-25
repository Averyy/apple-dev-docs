# init(_:)

**Framework**: Evaluations  
**Kind**: init

Creates a metric with just a name.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

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