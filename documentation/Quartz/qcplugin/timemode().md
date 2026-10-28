# timeMode()

**Framework**: Quartz  
**Kind**: method  
**Role**: Type Method

Returns the time mode for the custom patch.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class func timeMode() -> QCPlugInTimeMode
```

```objc
+ (QCPlugInTimeMode) timeMode;
```

## Return Value

The time mode of the custom patch. See [`QCPlugInTimeMode`](../qcplugintimemode.md) for the constants you can return.

## Discussion

You must implement this method to define whether you custom patch depends on time, doesn’t depend on time, or needs time to idle.

## See Also

### Defining the Characteristics of a Custom Patch
- [class func executionMode() -> QCPlugInExecutionMode](./executionmode%28%29.md)
  Returns the execution mode of the custom patch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin/timemode())*