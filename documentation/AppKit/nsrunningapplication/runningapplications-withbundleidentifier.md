# runningApplications(withBundleIdentifier:)

**Framework**: AppKit  
**Kind**: method

Returns an array of currently running applications with the specified bundle identifier.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class func runningApplications(withBundleIdentifier bundleIdentifier: String) -> [NSRunningApplication]
```

## Mentions

- [Passing control from one app to another with cooperative activation](passing-control-from-one-app-to-another-with-cooperative-activation.md)

#### Return Value

An array of `NSRunningApplications`, or an empty array if no applications match the bundle identifier.

## Parameters

- `bundleIdentifier`: The bundle identifier.

## See Also

- [convenience init?(processIdentifier: pid_t)](nsrunningapplication/init(processidentifier:).md)
  Returns the running application with the given process identifier, or nil if no application has that pid.
- [class var current: NSRunningApplication](nsrunningapplication/current.md)
  Returns an `NSRunningApplication` representing this application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/runningapplications(withbundleidentifier:))*