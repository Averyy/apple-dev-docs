# init()

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

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

Available when `Element` conforms to `Hashable`.

#### Discussion

This is equivalent to initializing with an empty array literal. For example:

```swift
var emptySet = Set<Int>()
print(emptySet.isEmpty)
// Prints "true"

emptySet = []
print(emptySet.isEmpty)
// Prints "true"
```

## See Also

### Creating a Set
- [init(minimumCapacity: Int)](./init%28minimumcapacity%29.md)
  Creates an empty set with preallocated space for at least the specified number of elements.
- [init<S>(S)](./init%28_%29-9cgks.md)
  Creates a new set from a finite sequence of items.
- [init<Source>(Source)](./init%28_%29.md)
  Creates a new set from a finite sequence of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/init())*