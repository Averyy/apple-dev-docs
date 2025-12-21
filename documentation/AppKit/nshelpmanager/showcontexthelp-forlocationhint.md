# showContextHelp(for:locationHint:)

**Framework**: AppKit  
**Kind**: method

Displays the context-sensitive help for a given object at or near the point on the screen specified by a given point.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func showContextHelp(for object: Any, locationHint pt: NSPoint) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) when help content is successfully displayed. [`false`](https://developer.apple.com/documentation/Swift/false) if help content is not displayed (for example, when there is no context-sensitive help associated with `object`).

## Parameters

- `object`: Object for which context-sensitive help is sought.
- `pt`: Screen location at which to display the help content; it’s usually under the cursor.

## See Also

- [func contextHelp(for: Any) -> NSAttributedString?](nshelpmanager/contexthelp(for:).md)
  Returns context-sensitive help for an object.
- [NSHelpManager.ContextHelpKey](nshelpmanager/contexthelpkey.md)
- [class var isContextHelpModeActive: Bool](nshelpmanager/iscontexthelpmodeactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/showcontexthelp(for:locationhint:))*