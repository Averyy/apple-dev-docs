# init(minimumCapacity:)

**Framework**: Swift  
**Kind**: init

Creates an empty set with preallocated space for at least the specified number of elements.

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
init(minimumCapacity: Int)
```

#### Discussion

Use this initializer to avoid intermediate reallocations of a set’s storage buffer when you know how many elements you’ll insert into the set after creation.

## Parameters

- `minimumCapacity`: The minimum number of elements that the   newly created set should be able to store without reallocating its   storage buffer.

## See Also

- [init()](set/init.md)
  Creates an empty set.
- [init<S>(S)](set/init(_:)-9cgks.md)
  Creates a new set from a finite sequence of items.
- [init<Source>(Source)](set/init(_:).md)
  Creates a new set from a finite sequence of items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/set/init(minimumcapacity:))*