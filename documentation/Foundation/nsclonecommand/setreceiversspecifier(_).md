# setReceiversSpecifier(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sets the receiver’s object specifier;.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func setReceiversSpecifier(_ receiversRef: NSScriptObjectSpecifier?)
```

```objc
- (void) setReceiversSpecifier:(NSScriptObjectSpecifier *) receiversRef;
```

## Discussion

When evaluated, the specifier indicates the receiver or receivers of the `clone` command.

This method overrides [`receiversSpecifier`](../nsscriptcommand/receiversspecifier.md) in [`NSScriptCommand`](../nsscriptcommand.md). It performs the same function as the overridden method, with a critical difference: it causes the container specifier part of the passed-in object specifier to become the receiver specifier of the command, and the key part of the passed-in object specifier to become the key specifier. If, for example, `receiversRef` is a specifier for `the third rectangle of the first document`, the receiver specifier is `the first document` while the key specifier is `the third rectangle`.

## Parameters

- `receiversRef`: The object specifier for the receiver.

## See Also

### Working with specifiers
- [var keySpecifier: NSScriptObjectSpecifier](./keyspecifier.md)
  Returns a specifier for the object or objects to be cloned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsclonecommand/setreceiversspecifier(_:))*