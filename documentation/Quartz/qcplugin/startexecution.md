# startExecution(_:)

**Framework**: Quartz  
**Kind**: method

Allows you to perform custom setup tasks before the Quartz Composer engine starts rendering.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func startExecution(_ context: (any QCPlugInContext)!) -> Bool
```

#### Return Value

[`false`](https://developer.apple.com/documentation/swift/false) indicates a fatal error occurred and prevents the Quartz Composer engine from starting.

#### Discussion

The Quartz Composer engine calls this method  when your custom patch starts to render. You can optionally override this execution method to perform setup tasks.

## Parameters

- `context`: An opaque object , conforming to the   protocol, that represents the execution context of the   object. Do not retain this object or use it outside of the scope of this method.

## See Also

- [func enableExecution((any QCPlugInContext)!)](qcplugin/enableexecution(_:).md)
  Allows you to perform custom tasks when the execution of the `QCPlugIn` object is resumed.
- [func disableExecution((any QCPlugInContext)!)](qcplugin/disableexecution(_:).md)
  Allows you to perform custom tasks when the execution of the `QCPlugIn` object is paused.
- [func stopExecution((any QCPlugInContext)!)](qcplugin/stopexecution(_:).md)
  Allows you to perform custom tasks when the `QCPlugIn` object stops executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/startexecution(_:))*