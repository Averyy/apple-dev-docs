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

When the command is executed, it sets attributes or relationships in the objects specified by `receiversRef`.

This method overrides [`receiversSpecifier`](nsscriptcommand/receiversspecifier.md) in [`NSScriptCommand`](nsscriptcommand.md). It performs the same function as the overridden method, with a critical difference: it causes the container specifier part of the passed-in object specifier to become the receiver specifier of the command, and the key part of the passed-in object specifier to become the key specifier. If, for example, `receiversRef` is a specifier for `the color of the third rectangle`, the receiver specifier is `the third rectangle,` while the key specifier is `the color`.

## Parameters

- `receiversRef`: The receiver’s object specifier.

## See Also

- [var keySpecifier: NSScriptObjectSpecifier](nssetcommand/keyspecifier.md)
  Returns a specifier that identifies the attribute or relationship that is to be set for the receiver of the `set` AppleScript command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssetcommand/setreceiversspecifier(_:))*