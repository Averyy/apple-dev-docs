# init()

**Framework**: Swift  
**Kind**: init

Creates a new, empty array.

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
init()
```

#### Discussion

This is equivalent to initializing with an empty array literal. For example:

```swift
var emptyArray = Array<Int>()
print(emptyArray.isEmpty)
// Prints "true"

emptyArray = []
print(emptyArray.isEmpty)
// Prints "true"
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/init())*