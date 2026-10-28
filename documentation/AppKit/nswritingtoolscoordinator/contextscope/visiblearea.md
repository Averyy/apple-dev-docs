# NSWritingToolsCoordinator.ContextScope.visibleArea

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

An option to provide only the text in the currently visible portion of your view.

**Availability**:
- macOS 15.2+

## Declaration

```swift
case visibleArea
```

```c
NSWritingToolsCoordinatorContextScopeVisibleArea
```

## Discussion

With this option, include only the currently visible text, along with some additional text before and after the visible text.

## See Also

### Getting the scope
- [NSWritingToolsCoordinator.ContextScope.userSelection](./userselection.md)
  An option to provide only the view’s currently selected text.
- [NSWritingToolsCoordinator.ContextScope.fullDocument](./fulldocument.md)
  An option to provide all of your view’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/contextscope/visiblearea)*