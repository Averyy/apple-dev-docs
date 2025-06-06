# timeMode()

**Framework**: Quartz  
**Kind**: method

Returns the time mode for the custom patch.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func timeMode() -> QCPlugInTimeMode
```

#### Return Value

The time mode of the custom patch. See [`QCPlugInTimeMode`](qcplugintimemode.md) for the constants you can return.

#### Discussion

You must implement this method to define whether you custom patch depends on time, doesn’t depend on time, or needs time to idle.

## See Also

- [class func executionMode() -> QCPlugInExecutionMode](qcplugin/executionmode.md)
  Returns the execution mode of the custom patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/timemode())*