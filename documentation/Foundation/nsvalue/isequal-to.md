# isEqual(to:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether the value object and another value object are equal.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func isEqual(to value: NSValue) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if both value objects are equal; otherwise, [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

The [`NSValue`](nsvalue.md) class compares the type and contents of each value object to determine equality.

## Parameters

- `value`: The other value object with which to compare the value object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/isequal(to:))*