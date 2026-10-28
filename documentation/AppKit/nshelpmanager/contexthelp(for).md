# contextHelp(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns context-sensitive help for an object.

**Availability**:
- macOS

## Declaration

```swift
func contextHelp(for object: Any) -> NSAttributedString?
```

```objc
- (NSAttributedString *) contextHelpForObject:(id) object;
```

## Return Value

Context-sensitive help content.

## Parameters

- `object`: Object for which context-sensitive help is sought.

## See Also

### Related Documentation
- [func setContextHelp(NSAttributedString, for: Any)](./setcontexthelp%28_,for%29.md)
  Associates help content with an object.
### Displaying Context-Sensitive Help
- [func showContextHelp(for: Any, locationHint: NSPoint) -> Bool](./showcontexthelp%28for,locationhint%29.md)
  Displays the context-sensitive help for a given object at or near the point on the screen specified by a given point.
- [NSHelpManager.ContextHelpKey](./contexthelpkey.md)
- [class var isContextHelpModeActive: Bool](./iscontexthelpmodeactive.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/contexthelp(for:))*