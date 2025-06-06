# isCaseInsensitiveLike(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Returns a Boolean value that indicates whether receiver is considered to be “like” a given string when the case of characters in the receiver is ignored.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
func isCaseInsensitiveLike(_ object: String) -> Bool
```

#### Return Value

[`YES`](yes.md) if the receiver is considered to be “like” `aString` when the case of characters in the receiver is ignored, otherwise [`NO`](no.md).

#### Discussion

Currently, [`isCaseInsensitiveLike(_:)`](nsobject-swift.class/iscaseinsensitivelike(_:).md) messages are never sent to any object from within Cocoa itself.

The default implementation for this method provided by `NSObject` returns [`NO`](no.md). `NSString` also provides an implementation of this method, which returns [`YES`](yes.md) if the receiver matches a pattern described by `aString`, ignoring the case of the characters in the receiver.

## Parameters

- `object`: The string with which to compare the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/iscaseinsensitivelike(_:))*