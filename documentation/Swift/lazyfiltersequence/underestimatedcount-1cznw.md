# underestimatedCount

**Framework**: Swift  
**Kind**: property

A value less than or equal to the number of elements in the sequence, calculated nondestructively.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var underestimatedCount: Int { get }
```

#### Discussion

The default implementation returns 0. If you provide your own implementation, make sure to compute the value nondestructively.

> **Note**: O(1), except if the sequence also conforms to `Collection`. In this case, see the documentation of `Collection.underestimatedCount`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/lazyfiltersequence/underestimatedcount-1cznw)*