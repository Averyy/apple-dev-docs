# setContextHelp(_:for:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Associates help content with an object.

**Availability**:
- macOS

## Declaration

```swift
func setContextHelp(_ attrString: NSAttributedString, for object: Any)
```

```objc
- (void) setContextHelp:(NSAttributedString *) attrString forObject:(id) object;
```

#### Discussion

When the application enters context-sensitive help mode, if `object` is clicked, `help` appears in the context-sensitive help window.

## Parameters

- `attrString`: Help content to associate with `object`.
- `object`: Object to associate with `help`.

## See Also

### Configuring Context-Sensitive Help
- [func removeContextHelp(for: Any)](./removecontexthelp%28for%29.md)
  Removes the association between an object and its context-sensitive help.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nshelpmanager/setcontexthelp(_:for:))*