# textFirstRect

**Framework**: BrowserEngineKit  
**Kind**: property  
**Required**: Yes

Returns a rect representing the bounds of the first line of marked text, if marked text is set.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var textFirstRect: CGRect { get }
```

#### Discussion

Otherwise, this returns a rect representing the bounds of the last word at or before the insertion point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/textfirstrect)*