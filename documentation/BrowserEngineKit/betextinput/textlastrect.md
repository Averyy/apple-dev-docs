# textLastRect

**Framework**: BrowserEngineKit  
**Kind**: property  
**Required**: Yes

Returns a rect representing the bounds of the last line of marked text, if marked text is set.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var textLastRect: CGRect { get }
```

#### Discussion

Otherwise, this returns a rect representing the bounds of the last word at or before the insertion point. This may have the same value of `textFirstRect`, but can differ in cases such as a word that spans two lines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/textlastrect)*