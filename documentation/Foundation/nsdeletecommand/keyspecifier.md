# keySpecifier

**Framework**: Foundation  
**Kind**: property

Returns a specifier for the object or objects to be deleted.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var keySpecifier: NSScriptObjectSpecifier { get }
```

#### Return Value

A specifier for the object or objects to be deleted.

#### Discussion

Note that this may be different than the specifier or specifiers set by [`setReceiversSpecifier(_:)`](nsdeletecommand/setreceiversspecifier(_:).md).

## See Also

- [Cocoa Scripting Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
- [Key-Value Coding Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)
- [func setReceiversSpecifier(NSScriptObjectSpecifier?)](nsdeletecommand/setreceiversspecifier(_:).md)
  Sets the receiver’s object specifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsdeletecommand/keyspecifier)*