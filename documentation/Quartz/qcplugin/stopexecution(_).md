# stopExecution(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Allows you to perform custom tasks when the `QCPlugIn` object stops executing.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func stopExecution(_ context: (any QCPlugInContext)!)
```

```objc
- (void) stopExecution:(id<QCPlugInContext>) context;
```

#### Discussion

The Quartz Composer engine calls this method when it stops executing. You can optionally override this execution method to perform cleanup tasks.

## Parameters

- `context`: An opaque object , conforming to the [`QCPlugInContext`](../qcplugincontext.md) protocol, that represents the execution context of the `QCPlugIn` object. Do not retain this object or use it outside of the scope of this method.

## See Also

### Performing Custom Tasks During Execution
- [func startExecution((any QCPlugInContext)!) -> Bool](./startexecution%28_%29.md)
  Allows you to perform custom setup tasks before the Quartz Composer engine starts rendering.
- [func enableExecution((any QCPlugInContext)!)](./enableexecution%28_%29.md)
  Allows you to perform custom tasks when the execution of the `QCPlugIn` object is resumed.
- [func disableExecution((any QCPlugInContext)!)](./disableexecution%28_%29.md)
  Allows you to perform custom tasks when the execution of the `QCPlugIn` object is paused.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/stopexecution(_:))*