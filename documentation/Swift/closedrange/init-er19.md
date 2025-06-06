# init(_:)

**Framework**: Swift  
**Kind**: init

Creates an instance equivalent to the given `Range`.

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
init(_ other: Range<Bound>)
```

#### Discussion

An equivalent range must be representable as a closed range. For example, passing an empty range as `other` triggers a runtime error, because an empty range cannot be represented by a closed range instance.

## Parameters

- `other`: A   to convert to a   instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/closedrange/init(_:)-er19)*