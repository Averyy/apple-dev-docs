# keySpecifier

**Framework**: Foundation  
**Kind**: property

Returns a specifier for the object or objects to be cloned.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var keySpecifier: NSScriptObjectSpecifier { get }
```

#### Return Value

A specifier for the object or objects to be cloned.

#### Discussion

For example, the specifier may indicate that a document’s third rectangle should be cloned. The returned specifier is valid only in the context of the `NSCloneCommand` object; for example, if you send the specifier a [`container`](nsscriptobjectspecifier/container.md) message, the result is `nil`.

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
- [func setReceiversSpecifier(NSScriptObjectSpecifier?)](nsclonecommand/setreceiversspecifier(_:).md)
  Sets the receiver’s object specifier;.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsclonecommand/keyspecifier)*