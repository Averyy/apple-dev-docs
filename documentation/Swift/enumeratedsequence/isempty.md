# isEmpty

**Framework**: Swift  
**Kind**: property

A Boolean value indicating whether the collection is empty.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var isEmpty: Bool { get }
```

#### Discussion

When you need to check whether your collection is empty, use the `isEmpty` property instead of checking that the `count` property is equal to zero. For collections that don’t conform to `RandomAccessCollection`, accessing the `count` property iterates through the elements of the collection.

```swift
let horseName = "Silver"
if horseName.isEmpty {
    print("My horse has no name.")
} else {
    print("Hi ho, \(horseName)!")
}
// Prints "Hi ho, Silver!"
```

> **Note**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/enumeratedsequence/isempty)*