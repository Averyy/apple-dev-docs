# appleEventCode(forKey:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns the Apple event code for the specified attribute or relationship in the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func appleEventCode(forKey key: String) -> FourCharCode
```

```objc
- (FourCharCode) appleEventCodeForKey:(NSString *) key;
```

## Return Value

The four-character Apple event code associated with the attribute or relationship identified by `key` in the receiver or, if none exists, in the class description for the receiver’s superclass. Returns `0` if no such attribute or relationship is found.

## Parameters

- `key`: The identifying key for an attribute or relationship of the receiver.

## See Also

### Getting and comparing Apple event codes
- [var appleEventCode: FourCharCode](./appleeventcode.md)
  Returns the Apple event code associated with the receiver’s class.
- [func matchesAppleEventCode(FourCharCode) -> Bool](./matchesappleeventcode%28_%29.md)
  Returns a Boolean value indicating whether a primary or secondary Apple event code in the receiver matches the passed code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptclassdescription/appleeventcode(forkey:))*