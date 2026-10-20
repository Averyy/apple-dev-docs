# keySpecifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns a specifier for the object or objects to be moved.

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

A specifier for the object or objects to be moved.

#### Discussion

Note that this specifier may be different than the specifier set by [`setReceiversSpecifier(_:)`](./setreceiversspecifier%28_%29.md), which sets the container specifier. For example, for a command such as `move the third circle to the location of the first circle`, the receiver might identify a document (which has a list of graphics), while the key specifier identifies the particular graphic to be moved.

## See Also

### Related Documentation
- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
### Working with specifiers
- [func setReceiversSpecifier(NSScriptObjectSpecifier?)](./setreceiversspecifier%28_%29.md)
  Sets the receiver’s object specifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsmovecommand/keyspecifier)*