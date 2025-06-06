# matchesAppleEventCode(_:)

**Framework**: Foundation  
**Kind**: method

Returns a Boolean value indicating whether a primary or secondary Apple event code in the receiver matches the passed code.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func matchesAppleEventCode(_ appleEventCode: FourCharCode) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver’s primary four-character Apple event code or any of its secondary codes (its synonyms) matches `code`; otherwise, [`false`](https://developer.apple.com/documentation/swift/false).

## Parameters

- `appleEventCode`: An Apple event code to compare against the receiver’s primary or secondary codes.

## See Also

- [var appleEventCode: FourCharCode](nsscriptclassdescription/appleeventcode.md)
  Returns the Apple event code associated with the receiver’s class.
- [func appleEventCode(forKey: String) -> FourCharCode](nsscriptclassdescription/appleeventcode(forkey:).md)
  Returns the Apple event code for the specified attribute or relationship in the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/matchesappleeventcode(_:))*