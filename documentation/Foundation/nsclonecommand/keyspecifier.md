# keySpecifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns a specifier for the object or objects to be cloned.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var keySpecifier: NSScriptObjectSpecifier { get }
```

```objc
@property (retain, readonly) NSScriptObjectSpecifier * keySpecifier;
```

#### Return Value

A specifier for the object or objects to be cloned.

#### Discussion

For example, the specifier may indicate that a document’s third rectangle should be cloned. The returned specifier is valid only in the context of the `NSCloneCommand` object; for example, if you send the specifier a [`container`](../nsscriptobjectspecifier/container.md) message, the result is `nil`.

## See Also

### Related Documentation
- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
### Working with specifiers
- [func setReceiversSpecifier(NSScriptObjectSpecifier?)](./setreceiversspecifier%28_%29.md)
  Sets the receiver’s object specifier;.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsclonecommand/keyspecifier)*