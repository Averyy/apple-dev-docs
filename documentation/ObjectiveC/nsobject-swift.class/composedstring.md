# composedString(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Return the current composed string.

**Availability**:
- macOS ?+

## Declaration

```swift
func composedString(_ sender: Any!) -> Any!
```

#### Return Value

The current composed string, which can be an `NSString` or `NSAttributedString` object. The returned object should be an autoreleased object.

#### Discussion

A composed string refers to the buffer that an input method typically maintains to mirror the text contained in the active inline area. It is called the composed string to reflect the fact that the input method composed the string by converting the characters input by the user. In addition, using the term composed string makes it easier to differentiate between an input method  buffer and the text in the active inline area that the user sees.

## Parameters

- `sender`: The client object requesting the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/composedstring(_:))*