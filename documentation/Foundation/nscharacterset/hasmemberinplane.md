# hasMemberInPlane(_:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether the receiver has at least one member in a given character plane.

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
func hasMemberInPlane(_ thePlane: UInt8) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver has at least one member in `thePlane`, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method makes it easier to find the plane containing the members of the current character set. The Basic Multilingual Plane (BMP) is plane `0`.

## Parameters

- `thePlane`: A character plane.

## See Also

- [func characterIsMember(unichar) -> Bool](nscharacterset/characterismember(_:).md)
  Returns a Boolean value that indicates whether a given character is in the receiver.
- [func isSuperset(of: CharacterSet) -> Bool](nscharacterset/issuperset(of:).md)
  Returns a Boolean value that indicates whether the receiver is a superset of another given character set.
- [func longCharacterIsMember(UTF32Char) -> Bool](nscharacterset/longcharacterismember(_:).md)
  Returns a Boolean value that indicates whether a given long character is a member of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/hasmemberinplane(_:))*