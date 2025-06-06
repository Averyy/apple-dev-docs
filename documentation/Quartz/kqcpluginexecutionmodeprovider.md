# kQCPlugInExecutionModeProvider

**Framework**: Quartz  
**Kind**: var

A provider execution mode. The custom patch executes on demand—that is, whenever data is requested of it, but at most once per frame.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var kQCPlugInExecutionModeProvider: QCPlugInExecutionMode { get }
```

## See Also

- [var kQCPlugInExecutionModeProcessor: QCPlugInExecutionMode](kqcpluginexecutionmodeprocessor.md)
  A processor execution mode. The custom patch executes whenever its inputs change or if the time change (assuming it’s time-dependent).
- [var kQCPlugInExecutionModeConsumer: QCPlugInExecutionMode](kqcpluginexecutionmodeconsumer.md)
  A consumer execution mode. The custom patch always executes assuming the value of its Enable input port is `true`. (The Enable port is automatically added by the system.)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/kqcpluginexecutionmodeprovider)*