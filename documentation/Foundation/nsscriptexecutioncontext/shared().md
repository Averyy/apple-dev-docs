# shared()

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the shared `NSScriptExecutionContext` instance.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
class func shared() -> NSScriptExecutionContext
```

```objc
+ (NSScriptExecutionContext *) sharedScriptExecutionContext;
```

#### Return Value

The shared `NSScriptExecutionContext` instance, creating it first if it doesn’t exist.

## See Also

### Related Documentation
- [Cocoa Scripting Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/ScriptableCocoaApplications/SApps_intro/SAppsIntro.html#//apple_ref/doc/uid/TP40002164)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptexecutioncontext/shared())*