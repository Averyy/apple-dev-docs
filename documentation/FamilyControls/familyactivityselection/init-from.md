# init(from:)

**Framework**: FamilyControls  
**Kind**: init

Creates a new instance by decoding from the given decoder.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+

## Declaration

```swift
init(from decoder: any Decoder) throws
```

#### Discussion

This initializer throws an error if reading from the decoder fails, or if the data read is corrupted or otherwise invalid.

## Parameters

- `decoder`: The decoder to read data from.

## See Also

- [init()](familyactivityselection/init.md)
  Creates a new activity selection instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivityselection/init(from:))*