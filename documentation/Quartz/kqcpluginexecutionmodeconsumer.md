# kQCPlugInExecutionModeConsumer

**Framework**: Quartz  
**Kind**: var

A consumer execution mode. The custom patch always executes assuming the value of its Enable input port is `true`. (The Enable port is automatically added by the system.)

**Availability**:
- macOS 10.4+

## Declaration

```swift
var kQCPlugInExecutionModeConsumer: QCPlugInExecutionMode { get }
```

## See Also

- [var kQCPlugInExecutionModeProvider: QCPlugInExecutionMode](kqcpluginexecutionmodeprovider.md)
  A provider execution mode. The custom patch executes on demand—that is, whenever data is requested of it, but at most once per frame.
- [var kQCPlugInExecutionModeProcessor: QCPlugInExecutionMode](kqcpluginexecutionmodeprocessor.md)
  A processor execution mode. The custom patch executes whenever its inputs change or if the time change (assuming it’s time-dependent).


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/kqcpluginexecutionmodeconsumer)*