# textUnfilteredPasteboardTypes

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an array of pasteboard types that can be loaded as text.

**Availability**:
- macOS 10.1+ - Deprecated in 10.5

> **Deprecated**: Use [`textUnfilteredTypes`](./textunfilteredtypes.md) instead.

## Declaration

```objc
+ (NSArray *) textUnfilteredPasteboardTypes;
```

## Return Value

An array of `NSString` objects, pasteboard types supported by text classes.

## Discussion

This list consists of all pasteboard types supported by text classes, but does not include those that can be converted to supported pasteboard types through a user-installed filter service.

## See Also

### Deprecated Properties
- [+ textFileTypes](./textfiletypes.md)
  Returns an array of strings that represent file types that can be loaded as text.
- [+ textUnfilteredFileTypes](./textunfilteredfiletypes.md)
  Returns an array of strings that represent file types that can be loaded as a text.
- [+ textPasteboardTypes](./textpasteboardtypes.md)
  Returns an array of pasteboard types that can be loaded as text.
- [var containsAttachments: Bool](./containsattachments.md)
  A Boolean value that indicates whether the attribute string contains any attachment attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/textunfilteredpasteboardtypes)*