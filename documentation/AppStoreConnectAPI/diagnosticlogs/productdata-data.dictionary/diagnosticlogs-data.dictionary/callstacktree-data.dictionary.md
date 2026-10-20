# diagnosticLogs.ProductData.DiagnosticLogs.CallStackTree

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The call stack representation of the diagnostic logs for single or multiple threads.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```
object diagnosticLogs.ProductData.DiagnosticLogs.CallStackTree
```

## Topics

### Objects
- [object diagnosticLogs.ProductData.DiagnosticLogs.CallStackTree.CallStacks](./callstacktree-data.dictionary/callstacks-data.dictionary.md)
  The root call stack frames of the diagnostic log.

## Properties

- `callStackPerThread` (boolean): A Boolean value that indicates whether the call stack representation supports multiple threads.
- `callStacks` ([diagnosticLogs.ProductData.DiagnosticLogs.CallStackTree.CallStacks]): The call stack representation of the diagnostic log.

## See Also

### Objects
- [object diagnosticLogs.ProductData.DiagnosticLogs.DiagnosticMetaData](./diagnosticmetadata-data.dictionary.md)
  Information about the diagnostic log including app version and build information, event details, OS, device type, and platform, and disk writes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/diagnosticlogs/productdata-data.dictionary/diagnosticlogs-data.dictionary/callstacktree-data.dictionary)*