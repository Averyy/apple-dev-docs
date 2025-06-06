# kQCPlugInTimeModeNone

**Framework**: Quartz  
**Kind**: var

No time dependency. The custom patch does not depend on time at all. (It does not use the `time`  parameter of the `execute:atTime:withArguments:` method.)

**Availability**:
- macOS 10.4+

## Declaration

```swift
var kQCPlugInTimeModeNone: QCPlugInTimeMode { get }
```

## See Also

- [var kQCPlugInTimeModeIdle: QCPlugInTimeMode](kqcplugintimemodeidle.md)
  An idle time dependency. The custom patch does not depend on time but needs the system to execute it periodically. For example if the custom patch connects to a piece of hardware, to ensure that it pulls data from the hardware, you would set the custom patch time dependency to idle time mode. This time mode is  typically used with providers.]]
- [var kQCPlugInTimeModeTimeBase: QCPlugInTimeMode](kqcplugintimemodetimebase.md)
  A time base dependency. The custom patch does depend on time explicitly and has a time base defined by the system. (It uses the `time`  parameter of the `execute:atTime:withArguments:` method.)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/kqcplugintimemodenone)*