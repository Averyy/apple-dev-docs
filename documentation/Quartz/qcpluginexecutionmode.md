# QCPlugInExecutionMode

**Framework**: Quartz  
**Kind**: struct

Execution modes for custom patches.

**Availability**:
- macOS 10.4+

## Declaration

```swift
struct QCPlugInExecutionMode
```

## Topics

### Constants
- [var kQCPlugInExecutionModeProvider: QCPlugInExecutionMode](kqcpluginexecutionmodeprovider.md)
  A provider execution mode. The custom patch executes on demand—that is, whenever data is requested of it, but at most once per frame.
- [var kQCPlugInExecutionModeProcessor: QCPlugInExecutionMode](kqcpluginexecutionmodeprocessor.md)
  A processor execution mode. The custom patch executes whenever its inputs change or if the time change (assuming it’s time-dependent).
- [var kQCPlugInExecutionModeConsumer: QCPlugInExecutionMode](kqcpluginexecutionmodeconsumer.md)
  A consumer execution mode. The custom patch always executes assuming the value of its Enable input port is `true`. (The Enable port is automatically added by the system.)
### Initializers
- [init(UInt32)](qcpluginexecutionmode/init(_:).md)
- [init(rawValue: UInt32)](qcpluginexecutionmode/init(rawvalue:).md)
### Instance Properties
- [var rawValue: UInt32](qcpluginexecutionmode/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct QCPlugInTimeMode](qcplugintimemode.md)
  Time modes for custom patches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcpluginexecutionmode)*