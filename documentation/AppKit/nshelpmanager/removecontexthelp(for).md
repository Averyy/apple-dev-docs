# removeContextHelp(for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Removes the association between an object and its context-sensitive help.

**Availability**:
- macOS

## Declaration

```swift
func removeContextHelp(for object: Any)
```

```objc
- (void) removeContextHelpForObject:(id) object;
```

## Discussion

If `object` does not have context-sensitive help associated with it, this method does nothing.

## Parameters

- `object`: Object to disassociate from its help content.

## See Also

### Configuring Context-Sensitive Help
- [func setContextHelp(NSAttributedString, for: Any)](./setcontexthelp%28_,for%29.md)
  Associates help content with an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/removecontexthelp(for:))*