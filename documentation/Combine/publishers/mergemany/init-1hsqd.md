# init(_:)

**Framework**: Combine  
**Kind**: init

Creates a publisher created by applying the merge function to an arbitrary number of upstream publishers.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(_ upstream: Upstream...)
```

## Parameters

- `upstream`: A variadic parameter containing zero or more publishers to merge with this publisher.

## See Also

- [init<S>(S)](publishers/mergemany/init(_:)-3hrmo.md)
  Creates a publisher created by applying the merge function to a sequence of upstream publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/mergemany/init(_:)-1hsqd)*