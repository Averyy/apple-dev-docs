# NSWritingToolsCoordinator.TextReplacementReason.temporary

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

An option to replace the text in your view when a grammar suggestion is temporarily shown to preview the proposed change in the text.

**Availability**:
- macOS 27.0+

## Declaration

```swift
case temporary
```

```c
NSWritingToolsCoordinatorTextReplacementReasonTemporary
```

#### Discussion

When the user interacts with a grammar issue and the UI is shown, in some cases the suggestion needs to be shown temporarily. Update your view’s text storage without animating the change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/textreplacementreason/temporary)*