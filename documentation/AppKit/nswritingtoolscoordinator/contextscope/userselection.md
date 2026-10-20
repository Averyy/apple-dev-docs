# NSWritingToolsCoordinator.ContextScope.userSelection

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

An option to provide only the view’s currently selected text.

**Availability**:
- macOS 15.2+

## Declaration

```swift
case userSelection
```

```c
NSWritingToolsCoordinatorContextScopeUserSelection
```

#### Discussion

With this option, include the selected text in your context object, along with some additional text before and after the selection. When performing changes inline with your view’s content, Writing Tools applies animations only to the selected text.

## See Also

### Getting the scope
- [NSWritingToolsCoordinator.ContextScope.fullDocument](./fulldocument.md)
  An option to provide all of your view’s text.
- [NSWritingToolsCoordinator.ContextScope.visibleArea](./visiblearea.md)
  An option to provide only the text in the currently visible portion of your view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswritingtoolscoordinator/contextscope/userselection)*