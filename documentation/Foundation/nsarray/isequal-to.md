# isEqual(to:)

**Framework**: Foundation  
**Kind**: method

Compares the receiving array to another array.

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
func isEqual(to otherArray: [Any]) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the contents of `otherArray` are equal to the contents of the receiving array, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

Two arrays have equal contents if they each hold the same number of objects and objects at a given index in each array satisfy the [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)) test.

## Parameters

- `otherArray`: An array.

## See Also

- [func firstObjectCommon(with: [Any]) -> Any?](nsarray/firstobjectcommon(with:).md)
  Returns the first object contained in the receiving array that’s equal to an object in another given array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/isequal(to:))*