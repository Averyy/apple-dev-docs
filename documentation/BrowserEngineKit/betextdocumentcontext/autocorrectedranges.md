# autocorrectedRanges

**Framework**: BrowserEngineKit  
**Kind**: property

Array of `NSRange` values, relative to the full context string made by combining the `contextBefore`, `markedText` (or `selectedText` if the marked text is empty), and the `contextAfter`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var autocorrectedRanges: [NSValue] { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextdocumentcontext/autocorrectedranges)*