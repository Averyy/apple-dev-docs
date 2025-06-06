# current

**Framework**: AppKit  
**Kind**: property

Returns an `NSRunningApplication` representing this application.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class var current: NSRunningApplication { get }
```

#### Return Value

An `NSRunningApplication` instance for the current application.

## See Also

- [convenience init?(processIdentifier: pid_t)](nsrunningapplication/init(processidentifier:).md)
  Returns the running application with the given process identifier, or nil if no application has that pid.
- [class func runningApplications(withBundleIdentifier: String) -> [NSRunningApplication]](nsrunningapplication/runningapplications(withbundleidentifier:).md)
  Returns an array of currently running applications with the specified bundle identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/current)*