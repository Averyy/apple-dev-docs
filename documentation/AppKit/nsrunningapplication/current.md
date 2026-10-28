# current

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns an `NSRunningApplication` representing this application.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class var current: NSRunningApplication { get }
```

```objc
@property (class, strong, readonly) NSRunningApplication * currentApplication;
```

## Return Value

An `NSRunningApplication` instance for the current application.

## See Also

### Getting running application instances
- [convenience init?(processIdentifier: pid_t)](./init%28processidentifier%29.md)
  Returns the running application with the given process identifier, or nil if no application has that pid.
- [class func runningApplications(withBundleIdentifier: String) -> [NSRunningApplication]](./runningapplications%28withbundleidentifier%29.md)
  Returns an array of currently running applications with the specified bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/current)*