# processID

**Framework**: ScreenCaptureKit  
**Kind**: property  
**Role**: Instance Property

The system process identifier of the app.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
var processID: pid_t { get }
```

```objc
@property (readonly) pid_t processID;
```

## See Also

### Inspecting an app
- [var bundleIdentifier: String](./bundleidentifier.md)
  The unique bundle identifier of the app.
- [var applicationName: String](./applicationname.md)
  The display name of the app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scrunningapplication/processid)*