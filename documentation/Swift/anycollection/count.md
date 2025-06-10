# count

**Framework**: Swift  
**Kind**: property

The number of elements.

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
var count: Int { get }
```

#### Discussion

To check whether a collection is empty, use its `isEmpty` property instead of comparing `count` to zero. Calculating `count` can be an O() operation.

> **Note**: O()


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anycollection/count)*