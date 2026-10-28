# appleEventCode

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the Apple event code associated with the receiver’s class.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var appleEventCode: FourCharCode { get }
```

```objc
@property (readonly) FourCharCode appleEventCode;
```

## Return Value

The Apple event code associated with the receiver’s class. This is the primary code used to identify the class in Apple events.

## See Also

### Getting and comparing Apple event codes
- [func appleEventCode(forKey: String) -> FourCharCode](./appleeventcode%28forkey%29.md)
  Returns the Apple event code for the specified attribute or relationship in the receiver.
- [func matchesAppleEventCode(FourCharCode) -> Bool](./matchesappleeventcode%28_%29.md)
  Returns a Boolean value indicating whether a primary or secondary Apple event code in the receiver matches the passed code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/appleeventcode)*