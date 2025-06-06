# contextHelp(for:)

**Framework**: AppKit  
**Kind**: method

Returns context-sensitive help for an object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func contextHelp(for object: Any) -> NSAttributedString?
```

#### Return Value

Context-sensitive help content.

## Parameters

- `object`: Object for which context-sensitive help is sought.

## See Also

- [func setContextHelp(NSAttributedString, for: Any)](nshelpmanager/setcontexthelp(_:for:).md)
  Associates help content with an object.
- [func showContextHelp(for: Any, locationHint: NSPoint) -> Bool](nshelpmanager/showcontexthelp(for:locationhint:).md)
  Displays the context-sensitive help for a given object at or near the point on the screen specified by a given point.
- [NSHelpManager.ContextHelpKey](nshelpmanager/contexthelpkey.md)
- [class var isContextHelpModeActive: Bool](nshelpmanager/iscontexthelpmodeactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/contexthelp(for:))*