# init(processIdentifier:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Returns the running application with the given process identifier, or nil if no application has that pid.

**Availability**:
- macOS 10.6+

## Declaration

```swift
convenience init?(processIdentifier pid: pid_t)
```

```objc
+ (instancetype) runningApplicationWithProcessIdentifier:(pid_t) pid;
```

## Return Value

An instance of `NSRunningApplication` for the specified `pid`, or nil if the application has no process identifier.

## Discussion

Applications that do not have `PIDs` cannot be returned from this method.

## Parameters

- `pid`: The process identifier.

## See Also

### Getting running application instances
- [class func runningApplications(withBundleIdentifier: String) -> [NSRunningApplication]](./runningapplications%28withbundleidentifier%29.md)
  Returns an array of currently running applications with the specified bundle identifier.
- [class var current: NSRunningApplication](./current.md)
  Returns an `NSRunningApplication` representing this application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/init(processidentifier:))*