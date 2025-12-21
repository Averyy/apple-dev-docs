# characterIsMember(_:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether a given character is in the receiver.

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
func characterIsMember(_ aCharacter: unichar) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if `aCharacter` is in the receiving character set, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

## Parameters

- `aCharacter`: The character to test for membership of the receiver.

## See Also

- [func hasMemberInPlane(UInt8) -> Bool](nscharacterset/hasmemberinplane(_:).md)
  Returns a Boolean value that indicates whether the receiver has at least one member in a given character plane.
- [func isSuperset(of: CharacterSet) -> Bool](nscharacterset/issuperset(of:).md)
  Returns a Boolean value that indicates whether the receiver is a superset of another given character set.
- [func longCharacterIsMember(UTF32Char) -> Bool](nscharacterset/longcharacterismember(_:).md)
  Returns a Boolean value that indicates whether a given long character is a member of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/characterismember(_:))*