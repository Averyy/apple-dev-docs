# capacity

**Framework**: Swift  
**Kind**: property

The total number of elements that the array can contain without allocating new storage.

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
var capacity: Int { get }
```

#### Discussion

Every array reserves a specific amount of memory to hold its contents. When you add elements to an array and that array begins to exceed its reserved capacity, the array allocates a larger region of memory and copies its elements into the new storage. The new storage is a multiple of the old storage’s size. This exponential growth strategy means that appending an element happens in constant time, averaging the performance of many append operations. Append operations that trigger reallocation have a performance cost, but they occur less and less often as the array grows larger.

The following example creates an array of integers from an array literal, then appends the elements of another collection. Before appending, the array allocates new storage that is large enough store the resulting elements.

```swift
var numbers = [10, 20, 30, 40, 50]
// numbers.count == 5
// numbers.capacity == 5

numbers.append(contentsOf: stride(from: 60, through: 100, by: 10))
// numbers.count == 10
// numbers.capacity == 10
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/contiguousarray/capacity)*