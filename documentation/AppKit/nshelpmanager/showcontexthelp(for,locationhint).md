# showContextHelp(for:locationHint:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays the context-sensitive help for a given object at or near the point on the screen specified by a given point.

**Availability**:
- macOS

## Declaration

```swift
func showContextHelp(for object: Any, locationHint pt: NSPoint) -> Bool
```

```objc
- (BOOL) showContextHelpForObject:(id) object locationHint:(NSPoint) pt;
```

#### Return Value

[`true`](../../Swift/true.md) when help content is successfully displayed. [`false`](../../Swift/false.md) if help content is not displayed (for example, when there is no context-sensitive help associated with `object`).

## Parameters

- `object`: Object for which context-sensitive help is sought.
- `pt`: Screen location at which to display the help content; it’s usually under the cursor.

## See Also

### Displaying Context-Sensitive Help
- [func contextHelp(for: Any) -> NSAttributedString?](./contexthelp%28for%29.md)
  Returns context-sensitive help for an object.
- [NSHelpManager.ContextHelpKey](./contexthelpkey.md)
- [class var isContextHelpModeActive: Bool](./iscontexthelpmodeactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/showcontexthelp(for:locationhint:))*