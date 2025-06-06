# stringEdited(in:changeInLength:)

**Framework**: Foundation  
**Kind**: method

Notifies the linguistic tagger that the string (if mutable) has changed as specified by the parameters.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func stringEdited(in newRange: NSRange, changeInLength delta: Int)
```

## Parameters

- `newRange`: The range in the final string that was edited.
- `delta`: The change in length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/stringedited(in:changeinlength:))*