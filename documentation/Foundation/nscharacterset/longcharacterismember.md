# longCharacterIsMember(_:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value that indicates whether a given long character is a member of the receiver.

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
func longCharacterIsMember(_ theLongChar: UTF32Char) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `theLongChar` is in the receiver, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method supports the specification of 32-bit characters.

## Parameters

- `theLongChar`: A UTF32 character.

## See Also

- [func characterIsMember(unichar) -> Bool](nscharacterset/characterismember(_:).md)
  Returns a Boolean value that indicates whether a given character is in the receiver.
- [func hasMemberInPlane(UInt8) -> Bool](nscharacterset/hasmemberinplane(_:).md)
  Returns a Boolean value that indicates whether the receiver has at least one member in a given character plane.
- [func isSuperset(of: CharacterSet) -> Bool](nscharacterset/issuperset(of:).md)
  Returns a Boolean value that indicates whether the receiver is a superset of another given character set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/longcharacterismember(_:))*