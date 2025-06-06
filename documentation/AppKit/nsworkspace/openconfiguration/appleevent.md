# appleEvent

**Framework**: AppKit  
**Kind**: property

The first Apple event to send to the new app.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var appleEvent: NSAppleEventDescriptor? { get set }
```

#### Discussion

The default value of this property is `nil`, which causes the system to send a default Apple event, as needed. The system sends the event only if an instance of the app is already running.

## See Also

- [var arguments: [String]](nsworkspace/openconfiguration/arguments.md)
  The set of command-line arguments to pass to a new app instance at launch time.
- [var environment: [String : String]](nsworkspace/openconfiguration/environment.md)
  The set of environment variables to set in a new app instance.
- [var architecture: cpu_type_t](nsworkspace/openconfiguration/architecture.md)
  The architecture version of the app to launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/appleevent)*