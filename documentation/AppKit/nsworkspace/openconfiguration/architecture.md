# architecture

**Framework**: AppKit  
**Kind**: property

The architecture version of the app to launch.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var architecture: cpu_type_t { get set }
```

#### Discussion

The default value of this property is `CPU_TYPE_ANY`, which causes the system to launch the app’s preferred architecture. You may specify a different value to force the system to launch that architecture. For a list of possible types, see the `<mach/machine.h>` header file.

## See Also

- [var appleEvent: NSAppleEventDescriptor?](nsworkspace/openconfiguration/appleevent.md)
  The first Apple event to send to the new app.
- [var arguments: [String]](nsworkspace/openconfiguration/arguments.md)
  The set of command-line arguments to pass to a new app instance at launch time.
- [var environment: [String : String]](nsworkspace/openconfiguration/environment.md)
  The set of environment variables to set in a new app instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/architecture)*