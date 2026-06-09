# textSelection

**Framework**: AppKit  
**Kind**: property  
**Required**: Yes

The current text selection.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
var textSelection: NSTextSelection? { get set }
```

#### Discussion

The text selection manager updates this property in response to user interactions. The delegate is responsible for storing and providing access to the current selection. The [`NSTextLocation`](nstextlocation.md) values that make up the [`NSTextRange`](nstextrange.md) objects can be any object that can describe a location in your text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextselectionmanager/delegate-swift.protocol/textselection)*