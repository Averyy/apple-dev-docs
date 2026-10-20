# dictionary()

**Framework**: AppKit  
**Kind**: method

Returns the print info’s dictionary that contains the printing attributes.

**Availability**:
- macOS ?+

## Declaration

```swift
func dictionary() -> NSMutableDictionary
```

#### Discussion

The key-value pairs contained in the dictionary are described in Constants. Modifying the returned dictionary changes the receiver’s attributes.

This dictionary is key-value observing compliant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintinfo/dictionary())*