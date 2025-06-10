# underestimatedCount

**Framework**: Create ML Components  
**Kind**: property

A value less than or equal to the number of elements in the sequence, calculated nondestructively.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var underestimatedCount: Int { get }
```

#### Discussion

The default implementation returns 0. If you provide your own implementation, make sure to compute the value nondestructively.

> **Note**: O(1), except if the sequence also conforms to `Collection`. In this case, see the documentation of `Collection.underestimatedCount`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/timeseriesforecasterbatches/underestimatedcount)*