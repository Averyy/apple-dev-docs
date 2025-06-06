# environment

**Framework**: AppKit  
**Kind**: property

The set of environment variables to set in a new app instance.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var environment: [String : String] { get set }
```

#### Discussion

The default value of this property is an empty dictionary. When launching a new instance of an app, use this property to specify the key/value pairs for any environment variables.

If the calling process is sandboxed, the system ignores the value of this property.

## See Also

- [var appleEvent: NSAppleEventDescriptor?](nsworkspace/openconfiguration/appleevent.md)
  The first Apple event to send to the new app.
- [var arguments: [String]](nsworkspace/openconfiguration/arguments.md)
  The set of command-line arguments to pass to a new app instance at launch time.
- [var architecture: cpu_type_t](nsworkspace/openconfiguration/architecture.md)
  The architecture version of the app to launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/environment)*