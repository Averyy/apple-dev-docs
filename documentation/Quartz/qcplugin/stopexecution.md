# stopExecution(_:)

**Framework**: Quartz  
**Kind**: method

Allows you to perform custom tasks when the `QCPlugIn` object stops executing.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func stopExecution(_ context: (any QCPlugInContext)!)
```

#### Discussion

The Quartz Composer engine calls this method when it stops executing. You can optionally override this execution method to perform cleanup tasks.

## Parameters

- `context`: An opaque object , conforming to the   protocol, that represents the execution context of the   object. Do not retain this object or use it outside of the scope of this method.

## See Also

- [func startExecution((any QCPlugInContext)!) -> Bool](qcplugin/startexecution(_:).md)
  Allows you to perform custom setup tasks before the Quartz Composer engine starts rendering.
- [func enableExecution((any QCPlugInContext)!)](qcplugin/enableexecution(_:).md)
  Allows you to perform custom tasks when the execution of the `QCPlugIn` object is resumed.
- [func disableExecution((any QCPlugInContext)!)](qcplugin/disableexecution(_:).md)
  Allows you to perform custom tasks when the execution of the `QCPlugIn` object is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/stopexecution(_:))*