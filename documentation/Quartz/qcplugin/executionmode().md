# executionMode()

**Framework**: Quartz  
**Kind**: method  
**Role**: Type Method

Returns the execution mode of the custom patch.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class func executionMode() -> QCPlugInExecutionMode
```

```objc
+ (QCPlugInExecutionMode) executionMode;
```

## Return Value

The execution mode of the custom patch. See [`QCPlugInExecutionMode`](../qcpluginexecutionmode.md) for the constants you can return.

## Discussion

You must implement this method to define whether your custom patch is a provider, a processor, or a consumer.

## See Also

### Defining the Characteristics of a Custom Patch
- [class func timeMode() -> QCPlugInTimeMode](./timemode%28%29.md)
  Returns the time mode for the custom patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/executionmode())*