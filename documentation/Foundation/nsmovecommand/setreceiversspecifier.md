# setReceiversSpecifier(_:)

**Framework**: Foundation  
**Kind**: method

Sets the receiver’s object specifier.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setReceiversSpecifier(_ receiversRef: NSScriptObjectSpecifier?)
```

#### Discussion

When evaluated, `receiversRef` indicates the receiver or receivers of the `move` AppleScript command.

This method overrides [`receiversSpecifier`](nsscriptcommand/receiversspecifier.md) in [`NSScriptCommand`](nsscriptcommand.md). It performs the same function as the overridden method, with a critical difference: it causes the container specifier part of the passed-in object specifier to become the receiver specifier of the command, and the key part of the passed-in object specifier to become the key specifier. If, for example, `receiversRef` is a specifier for `the third paragraph of the first document`, the receiver specifier is `the first document` while the key specifier is `the third paragraph`.

## Parameters

- `receiversRef`: The receiver’s object specifier.

## See Also

- [var keySpecifier: NSScriptObjectSpecifier](nsmovecommand/keyspecifier.md)
  Returns a specifier for the object or objects to be moved.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmovecommand/setreceiversspecifier(_:))*