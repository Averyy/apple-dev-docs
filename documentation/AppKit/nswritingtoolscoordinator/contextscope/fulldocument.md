# NSWritingToolsCoordinator.ContextScope.fullDocument

**Framework**: AppKit  
**Kind**: case

An option to provide all of your view’s text.

**Availability**:
- macOS 15.2+

## Declaration

```swift
case fullDocument
```

#### Discussion

With this option, include all of the text your view manages. If your view has multiple text storage objects, create a separate context object for each one.

## See Also

- [NSWritingToolsCoordinator.ContextScope.userSelection](nswritingtoolscoordinator/contextscope/userselection.md)
  An option to provide only the view’s currently selected text.
- [NSWritingToolsCoordinator.ContextScope.visibleArea](nswritingtoolscoordinator/contextscope/visiblearea.md)
  An option to provide only the text in the currently visible portion of your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/contextscope/fulldocument)*