# setShared(_:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Sets the single, shared instance of `NSScriptSuiteRegistry` to `registry`.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class func setShared(_ registry: NSScriptSuiteRegistry)
```

```objc
+ (void) setSharedScriptSuiteRegistry:(NSScriptSuiteRegistry *) registry;
```

## See Also

### Related Documentation
- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)
### Getting and Setting the Shared Instance
- [class func shared() -> NSScriptSuiteRegistry](./shared%28%29.md)
  Returns the single, shared instance of `NSScriptSuiteRegistry`, creating it first if it doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptsuiteregistry/setshared(_:))*