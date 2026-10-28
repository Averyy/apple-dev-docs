# startExecution(_:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Allows you to perform custom setup tasks before the Quartz Composer engine starts rendering.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
func startExecution(_ context: (any QCPlugInContext)!) -> Bool
```

```objc
- (BOOL) startExecution:(id<QCPlugInContext>) context;
```

## Return Value

[`false`](../../Swift/false.md) indicates a fatal error occurred and prevents the Quartz Composer engine from starting.

## Discussion

The Quartz Composer engine calls this method  when your custom patch starts to render. You can optionally override this execution method to perform setup tasks.

## Parameters

- `context`: An opaque object , conforming to the [`QCPlugInContext`](../qcplugincontext.md) protocol, that represents the execution context of the `QCPlugIn` object. Do not retain this object or use it outside of the scope of this method.

## See Also

### Performing Custom Tasks During Execution
- [func enableExecution((any QCPlugInContext)!)](./enableexecution%28_%29.md)
  Allows you to perform custom tasks when the execution of the `QCPlugIn` object is resumed.
- [func disableExecution((any QCPlugInContext)!)](./disableexecution%28_%29.md)
  Allows you to perform custom tasks when the execution of the `QCPlugIn` object is paused.
- [func stopExecution((any QCPlugInContext)!)](./stopexecution%28_%29.md)
  Allows you to perform custom tasks when the `QCPlugIn` object stops executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/startexecution(_:))*