# kCFSocketAutomaticallyReenableReadCallBack

**Framework**: Core Foundation  
**Kind**: var

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var kCFSocketAutomaticallyReenableReadCallBack: CFOptionFlags { get }
```

#### Discussion

When enabled using [`CFSocketSetSocketFlags(_:_:)`](cfsocketsetsocketflags(_:_:).md), the read callback is called every time the sockets has data to be read. When disabled, the read callback is called only once the next time data are available. The read callback is automatically reenabled by default.

## See Also

- [var kCFSocketAutomaticallyReenableAcceptCallBack: CFOptionFlags](kcfsocketautomaticallyreenableacceptcallback.md)
- [var kCFSocketAutomaticallyReenableDataCallBack: CFOptionFlags](kcfsocketautomaticallyreenabledatacallback.md)
- [var kCFSocketAutomaticallyReenableWriteCallBack: CFOptionFlags](kcfsocketautomaticallyreenablewritecallback.md)
- [var kCFSocketLeaveErrors: CFOptionFlags](kcfsocketleaveerrors.md)
- [var kCFSocketCloseOnInvalidate: CFOptionFlags](kcfsocketcloseoninvalidate.md)
  When enabled using [`CFSocketSetSocketFlags(_:_:)`](cfsocketsetsocketflags(_:_:).md), the native socket associated with a CFSocket object is closed when the CFSocket object is invalidated. When disabled, the native socket remains open. This option is enabled by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfsocketautomaticallyreenablereadcallback)*