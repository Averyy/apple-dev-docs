# disableExecution(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Allows you to perform custom tasks when the execution of the `QCPlugIn` object is paused.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func disableExecution(_ context: (any QCPlugInContext)!)
```

```objc
- (void) disableExecution:(id<QCPlugInContext>) context;
```

#### Discussion

The Quartz Composer engine calls this method when results are no longer being pulled from the  custom patch. You can optionally override this execution method to perform custom tasks at that time.

## Parameters

- `context`: An opaque object , conforming to the [`QCPlugInContext`](../qcplugincontext.md) protocol, that represents the execution context of the `QCPlugIn` object. Do not retain this object or use it outside of the scope of this method.

## See Also

### Performing Custom Tasks During Execution
- [func startExecution((any QCPlugInContext)!) -> Bool](./startexecution%28_%29.md)
  Allows you to perform custom setup tasks before the Quartz Composer engine starts rendering.
- [func enableExecution((any QCPlugInContext)!)](./enableexecution%28_%29.md)
  Allows you to perform custom tasks when the execution of the `QCPlugIn` object is resumed.
- [func stopExecution((any QCPlugInContext)!)](./stopexecution%28_%29.md)
  Allows you to perform custom tasks when the `QCPlugIn` object stops executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/disableexecution(_:))*