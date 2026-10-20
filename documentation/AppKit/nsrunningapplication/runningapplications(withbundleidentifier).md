# runningApplications(withBundleIdentifier:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns an array of currently running applications with the specified bundle identifier.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class func runningApplications(withBundleIdentifier bundleIdentifier: String) -> [NSRunningApplication]
```

```objc
+ (NSArray<NSRunningApplication *> *) runningApplicationsWithBundleIdentifier:(NSString *) bundleIdentifier;
```

## Mentions

- [Passing control from one app to another with cooperative activation](../passing-control-from-one-app-to-another-with-cooperative-activation.md)

#### Return Value

An array of `NSRunningApplications`, or an empty array if no applications match the bundle identifier.

## Parameters

- `bundleIdentifier`: The bundle identifier.

## See Also

### Getting running application instances
- [convenience init?(processIdentifier: pid_t)](./init%28processidentifier%29.md)
  Returns the running application with the given process identifier, or nil if no application has that pid.
- [class var current: NSRunningApplication](./current.md)
  Returns an `NSRunningApplication` representing this application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/runningapplications(withbundleidentifier:))*