# init()

**Framework**: Swift  
**Kind**: init  
**Role**: Initializer

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

## See Also

### Creating an Array
- [init<S>(S)](./init%28_%29-1ip9h.md)
  Creates a new instance of a collection containing the elements of a sequence.
- [init<S>(S)](./init%28_%29-236cl.md)
  Creates an array containing the elements of a sequence.
- [init(repeating: Element, count: Int)](./init%28repeating,count%29.md)
  Creates a new array containing the specified number of a single, repeated value.
- [init<E>(unsafeUninitializedCapacity: Int, initializingWith: (inout UnsafeMutableBufferPointer<Element>, inout Int) throws(E) -> Void) throws(E)](./init%28unsafeuninitializedcapacity,initializingwith%29.md)
  Creates an array with the specified capacity, and then calls the given closure with a buffer covering the array’s uninitialized memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/array/init())*