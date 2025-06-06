# removeContextHelp(for:)

**Framework**: AppKit  
**Kind**: method

Removes the association between an object and its context-sensitive help.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func removeContextHelp(for object: Any)
```

#### Discussion

If `object` does not have context-sensitive help associated with it, this method does nothing.

## Parameters

- `object`: Object to disassociate from its help content.

## See Also

- [func setContextHelp(NSAttributedString, for: Any)](nshelpmanager/setcontexthelp(_:for:).md)
  Associates help content with an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/removecontexthelp(for:))*