# init(capacity:copying:)

**Framework**: Swift  
**Kind**: init

Creates a new array with the specified capacity, holding a copy of the contents of the given span.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
init(capacity: Int? = nil, copying span: Span<Element>)
```

## Parameters

- `capacity`: The storage capacity of the new array, or nil to allocate just enough capacity to store the contents of the span.
- `span`: The span whose contents to copy into the new array. The span must not contain more than `capacity` elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/uniquearray/init(capacity:copying:)-991h4)*