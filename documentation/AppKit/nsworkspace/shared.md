# shared

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

The shared workspace object.

**Availability**:
- macOS

## Declaration

```swift
class var shared: NSWorkspace { get }
```

```objc
@property (class, strong, readonly) NSWorkspace * sharedWorkspace;
```

## Return Value

The `NSWorkspace` object associated with the process.

## Discussion

You can access this object safely from any thread in your app.

## See Also

### Related Documentation
- [Workspace Services Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Workspace/introduction.html#//apple_ref/doc/uid/10000100i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/shared)*