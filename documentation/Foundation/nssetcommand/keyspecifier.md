# keySpecifier

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns a specifier that identifies the attribute or relationship that is to be set for the receiver of the `set` AppleScript command.

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

A specifier that identifies the attribute or relationship that is to be set for the receiver of the `set` AppleScript command.

## See Also

### Related Documentation
- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
### Working with specifiers
- [func setReceiversSpecifier(NSScriptObjectSpecifier?)](./setreceiversspecifier%28_%29.md)
  Sets the receiver’s object specifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nssetcommand/keyspecifier)*