# init()

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer  
**Required**: Yes

Creates an empty set.

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

This initializer is equivalent to initializing with an empty array literal. For example, you create an empty `Set` instance with either this initializer or with an empty array literal.

```swift
var emptySet = Set<Int>()
print(emptySet.isEmpty)
// Prints "true"

emptySet = []
print(emptySet.isEmpty)
// Prints "true"
```

## Default Implementations

### SetAlgebra Implementations
- [init()](./init%28%29-3obov.md)
  Creates an empty option set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/setalgebra/init())*