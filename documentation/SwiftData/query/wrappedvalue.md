# wrappedValue

**Framework**: Swiftdata  
**Kind**: property

The most recent fetched result from the Query.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
@MainActor
@preconcurrency var wrappedValue: Result { get }
```

#### Discussion

> **Note**: When an fetch error occurs, `wrappedValue` retains results from the last successful fetch. Its value will update once a new fetch succeeds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftdata/query/wrappedvalue)*