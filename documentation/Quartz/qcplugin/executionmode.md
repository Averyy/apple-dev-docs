# executionMode()

**Framework**: Quartz  
**Kind**: method

Returns the execution mode of the custom patch.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class func executionMode() -> QCPlugInExecutionMode
```

#### Return Value

The execution mode of the custom patch. See [`QCPlugInExecutionMode`](qcpluginexecutionmode.md) for the constants you can return.

#### Discussion

You must implement this method to define whether your custom patch is a provider, a processor, or a consumer.

## See Also

- [class func timeMode() -> QCPlugInTimeMode](qcplugin/timemode.md)
  Returns the time mode for the custom patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/executionmode())*