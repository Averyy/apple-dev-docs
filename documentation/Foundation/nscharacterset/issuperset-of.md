# isSuperset(of:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether the receiver is a superset of another given character set.

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
func isSuperset(of theOtherSet: CharacterSet) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver is a superset of `theOtherSet`, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `theOtherSet`: A character set.

## See Also

- [func characterIsMember(unichar) -> Bool](nscharacterset/characterismember(_:).md)
  Returns a Boolean value that indicates whether a given character is in the receiver.
- [func hasMemberInPlane(UInt8) -> Bool](nscharacterset/hasmemberinplane(_:).md)
  Returns a Boolean value that indicates whether the receiver has at least one member in a given character plane.
- [func longCharacterIsMember(UTF32Char) -> Bool](nscharacterset/longcharacterismember(_:).md)
  Returns a Boolean value that indicates whether a given long character is a member of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/issuperset(of:))*