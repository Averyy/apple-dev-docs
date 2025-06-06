# appleEventCode

**Framework**: Foundation  
**Kind**: property

Returns the Apple event code associated with the receiver’s class.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var appleEventCode: FourCharCode { get }
```

#### Return Value

The Apple event code associated with the receiver’s class. This is the primary code used to identify the class in Apple events.

## See Also

- [func appleEventCode(forKey: String) -> FourCharCode](nsscriptclassdescription/appleeventcode(forkey:).md)
  Returns the Apple event code for the specified attribute or relationship in the receiver.
- [func matchesAppleEventCode(FourCharCode) -> Bool](nsscriptclassdescription/matchesappleeventcode(_:).md)
  Returns a Boolean value indicating whether a primary or secondary Apple event code in the receiver matches the passed code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/appleeventcode)*