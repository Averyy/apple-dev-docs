# arguments

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The set of command-line arguments to pass to a new app instance at launch time.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var arguments: [String] { get set }
```

```objc
@property (copy) NSArray<NSString *> * arguments;
```

#### Discussion

The default value of this property is an empty array. When launching a new instance of an app, use this property to specify any additional launch arguments. The system inserts the app’s path as the first element in the array.

If the calling process is sandboxed, the system ignores the value of this property.

## See Also

### Specifying launch attributes
- [var appleEvent: NSAppleEventDescriptor?](./appleevent.md)
  The first Apple event to send to the new app.
- [var environment: [String : String]](./environment.md)
  The set of environment variables to set in a new app instance.
- [var architecture: cpu_type_t](./architecture.md)
  The architecture version of the app to launch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/openconfiguration/arguments)*