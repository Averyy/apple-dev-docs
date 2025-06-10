# isEmpty

**Framework**: Create ML  
**Kind**: property

A Boolean value indicating whether the collection is empty.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var isEmpty: Bool { get }
```

#### Discussion

When you need to check whether your collection is empty, use the `isEmpty` property instead of checking that the `count` property is equal to zero. For collections that don’t conform to `RandomAccessCollection`, accessing the `count` property iterates through the elements of the collection.

```None
let horseName = "Silver"
if horseName.isEmpty {
    print("My horse has no name.")
} else {
    print("Hi ho, \(horseName)!")
}
// Prints "Hi ho, Silver!")
```

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldatatable/row/values-swift.struct/isempty)*