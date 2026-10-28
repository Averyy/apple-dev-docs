# architecture

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The architecture version of the app to launch.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var architecture: cpu_type_t { get set }
```

```objc
@property cpu_type_t architecture;
```

## Discussion

The default value of this property is `CPU_TYPE_ANY`, which causes the system to launch the app’s preferred architecture. You may specify a different value to force the system to launch that architecture. For a list of possible types, see the `<mach/machine.h>` header file.

## See Also

### Specifying launch attributes
- [var appleEvent: NSAppleEventDescriptor?](./appleevent.md)
  The first Apple event to send to the new app.
- [var arguments: [String]](./arguments.md)
  The set of command-line arguments to pass to a new app instance at launch time.
- [var environment: [String : String]](./environment.md)
  The set of environment variables to set in a new app instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/architecture)*