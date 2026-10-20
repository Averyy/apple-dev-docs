# characterIsMember(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) characterIsMember:(unichar) aCharacter;
```

#### Return Value

[`true`](../../Swift/true.md) if `aCharacter` is in the receiving character set, otherwise [`false`](../../Swift/false.md).

## Parameters

- `aCharacter`: The character to test for membership of the receiver.

## See Also

### Testing Set Membership
- [func hasMemberInPlane(UInt8) -> Bool](./hasmemberinplane%28_%29.md)
  Returns a Boolean value that indicates whether the receiver has at least one member in a given character plane.
- [func isSuperset(of: CharacterSet) -> Bool](./issuperset%28of%29.md)
  Returns a Boolean value that indicates whether the receiver is a superset of another given character set.
- [func longCharacterIsMember(UTF32Char) -> Bool](./longcharacterismember%28_%29.md)
  Returns a Boolean value that indicates whether a given long character is a member of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscharacterset/characterismember(_:))*