# textUnfilteredFileTypes

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns an array of strings that represent file types that can be loaded as a text.

**Availability**:
- macOS 10.1+ - Deprecated in 10.5

> **Deprecated**: Use [`textUnfilteredTypes`](./textunfilteredtypes.md) instead.

## Declaration

```objc
+ (NSArray *) textUnfilteredFileTypes;
```

## Return Value

An array of `NSString` objects, consisting of all file types supported by text classes, but does not include those types that can be converted to supported file types through a user-installed filter service.

## Discussion

This list consists of all file types supported by text classes, but does not include those types that can be converted to supported file types through a user-installed filter service. In macOS, the array returned by this method may be passed directly to the `runModalForTypes:` method of [`NSOpenPanel`](../../AppKit/nsopenpanel.md).

## See Also

### Deprecated Properties
- [+ textFileTypes](./textfiletypes.md)
  Returns an array of strings that represent file types that can be loaded as text.
- [+ textPasteboardTypes](./textpasteboardtypes.md)
  Returns an array of pasteboard types that can be loaded as text.
- [+ textUnfilteredPasteboardTypes](./textunfilteredpasteboardtypes.md)
  Returns an array of pasteboard types that can be loaded as text.
- [var containsAttachments: Bool](./containsattachments.md)
  A Boolean value that indicates whether the attribute string contains any attachment attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/textunfilteredfiletypes)*