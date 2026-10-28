# textPasteboardTypes

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an array of pasteboard types that can be loaded as text.

**Availability**:
- macOS 10.1+ - Deprecated in 10.5

> **Deprecated**: Use [`textTypes`](./texttypes.md) instead.

## Declaration

```objc
+ (NSArray *) textPasteboardTypes;
```

## Return Value

An array of `NSString` objects, containing the pasteboard types supported by text classes and those that can be converted to supported pasteboard types through a user-installed filter service.

## Discussion

By default, the list returned by this method includes `NSHTMLPboardType`, `NSRTFPboardType`, `NSRTFDPboardType`, and `NSStringPboardType`.

When creating a subclass of `NSAttributedString` that accepts text data from non-default pasteboard types, override [`textUnfilteredPasteboardTypes`](./textunfilteredpasteboardtypes.md) to notify `NSAttributedString` of the pasteboard types your class supports.

## See Also

### Deprecated Properties
- [+ textFileTypes](./textfiletypes.md)
  Returns an array of strings that represent file types that can be loaded as text.
- [+ textUnfilteredFileTypes](./textunfilteredfiletypes.md)
  Returns an array of strings that represent file types that can be loaded as a text.
- [+ textUnfilteredPasteboardTypes](./textunfilteredpasteboardtypes.md)
  Returns an array of pasteboard types that can be loaded as text.
- [var containsAttachments: Bool](./containsattachments.md)
  A Boolean value that indicates whether the attribute string contains any attachment attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/textpasteboardtypes)*