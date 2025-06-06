# setContextHelp(_:for:)

**Framework**: AppKit  
**Kind**: method

Associates help content with an object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func setContextHelp(_ attrString: NSAttributedString, for object: Any)
```

#### Discussion

When the application enters context-sensitive help mode, if `object` is clicked, `help` appears in the context-sensitive help window.

## Parameters

- `attrString`: Help content to associate with  .
- `object`: Object to associate with  .

## See Also

- [func removeContextHelp(for: Any)](nshelpmanager/removecontexthelp(for:).md)
  Removes the association between an object and its context-sensitive help.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/setcontexthelp(_:for:))*