# firstObjectCommon(with:)

**Framework**: Foundation  
**Kind**: method

Returns the first object contained in the receiving array that’s equal to an object in another given array.

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
func firstObjectCommon(with otherArray: [Any]) -> Any?
```

#### Return Value

Returns the first object contained in the receiving array that’s equal to an object in `otherArray`. If no such object is found, returns `nil`.

#### Discussion

This method uses [`isEqual(_:)`](https://developer.apple.com/documentation/ObjectiveC/NSObjectProtocol/isEqual(_:)) to check for object equality.

## Parameters

- `otherArray`: An array.

## See Also

- [func contains(Any) -> Bool](nsarray/contains(_:).md)
  Returns a Boolean value that indicates whether a given object is present in the array.
- [func isEqual(to: [Any]) -> Bool](nsarray/isequal(to:).md)
  Compares the receiving array to another array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsarray/firstobjectcommon(with:))*