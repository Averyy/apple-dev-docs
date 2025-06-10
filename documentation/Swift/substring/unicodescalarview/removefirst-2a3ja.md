# removeFirst()

**Framework**: Swift  
**Kind**: method

Removes and returns the first element of the collection.

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
@discardableResult
mutating func removeFirst() -> Self.Element
```

#### Return Value

The removed element.

#### Discussion

The collection must not be empty.

```swift
var bugs = ["Aphid", "Bumblebee", "Cicada", "Damselfly", "Earwig"]
bugs.removeFirst()
print(bugs)
// Prints "["Bumblebee", "Cicada", "Damselfly", "Earwig"]"
```

Calling this method may invalidate any existing indices for use with this collection.

> **Note**: O(), where  is the length of the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/substring/unicodescalarview/removefirst()-2a3ja)*