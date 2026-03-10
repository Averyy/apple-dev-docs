# kCTTabColumnTerminatorsAttributeName

**Framework**: Core Text  
**Kind**: var

Specifies the terminating character for a tab column.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCTTabColumnTerminatorsAttributeName: CFString
```

#### Discussion

The value associated with this attribute is a [`CFCharacterSet`](https://developer.apple.com/documentation/CoreFoundation/CFCharacterSet) object. The character set is used to determine the terminating character for a tab column. The tab and newline characters are implied even if they don’t exist in the character set. This attribute can be used to implement decimal tabs, for instance. This attribute is optional.

## See Also

- [func CTTextTabCreate(CTTextAlignment, Double, CFDictionary?) -> CTTextTab](cttexttabcreate(_:_:_:).md)
  Creates and initializes a new text tab object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kcttabcolumnterminatorsattributename)*