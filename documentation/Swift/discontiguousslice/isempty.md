# isEmpty

**Framework**: Swift  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the collection is empty.

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
var isEmpty: Bool { get }
```

Available when `Base` conforms to `Collection`.

## Discussion

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

> **Complexity**: O(1)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/discontiguousslice/isempty)*