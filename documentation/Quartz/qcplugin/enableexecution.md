# enableExecution(_:)

**Framework**: Quartz  
**Kind**: method

Allows you to perform custom tasks when the execution of the `QCPlugIn` object is resumed.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func enableExecution(_ context: (any QCPlugInContext)!)
```

#### Discussion

The Quartz Composer engine calls this method  when results start to be pulled from the  custom patch. You can optionally override this execution method to perform custom tasks at that time.

## Parameters

- `context`: An opaque object , conforming to the   protocol, that represents the execution context of the   object. Do not retain this object or use it outside of the scope of this method.

## See Also

- [func startExecution((any QCPlugInContext)!) -> Bool](qcplugin/startexecution(_:).md)
  Allows you to perform custom setup tasks before the Quartz Composer engine starts rendering.
- [func disableExecution((any QCPlugInContext)!)](qcplugin/disableexecution(_:).md)
  Allows you to perform custom tasks when the execution of the `QCPlugIn` object is paused.
- [func stopExecution((any QCPlugInContext)!)](qcplugin/stopexecution(_:).md)
  Allows you to perform custom tasks when the `QCPlugIn` object stops executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/enableexecution(_:))*