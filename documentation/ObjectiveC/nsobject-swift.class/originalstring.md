# originalString(_:)

**Framework**: Objective-C Runtime  
**Kind**: method

Return the string that consists of the precomposed Unicode characters.

**Availability**:
- macOS ?+

## Declaration

```swift
func originalString(_ sender: Any!) -> NSAttributedString!
```

#### Return Value

The original string of precomposed unicode characters. If an input method stores the original input text, it returns that text. The return value is an attributed string so that the input method can restore changes they made to the font, and other attributes, if necessary. The returned object should be an autoreleased object.

## Parameters

- `sender`: The client object requesting the original string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/objectivec/nsobject-swift.class/originalstring(_:))*