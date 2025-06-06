# kCFSocketAutomaticallyReenableDataCallBack

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
var kCFSocketAutomaticallyReenableDataCallBack: CFOptionFlags { get }
```

#### Discussion

When enabled using [`CFSocketSetSocketFlags(_:_:)`](cfsocketsetsocketflags(_:_:).md), the data callback is called every time the socket has read some data. When disabled, the data callback is called only once the next time data are read. The data callback is automatically reenabled by default.

## See Also

- [var kCFSocketAutomaticallyReenableReadCallBack: CFOptionFlags](kcfsocketautomaticallyreenablereadcallback.md)
- [var kCFSocketAutomaticallyReenableAcceptCallBack: CFOptionFlags](kcfsocketautomaticallyreenableacceptcallback.md)
- [var kCFSocketAutomaticallyReenableWriteCallBack: CFOptionFlags](kcfsocketautomaticallyreenablewritecallback.md)
- [var kCFSocketLeaveErrors: CFOptionFlags](kcfsocketleaveerrors.md)
- [var kCFSocketCloseOnInvalidate: CFOptionFlags](kcfsocketcloseoninvalidate.md)
  When enabled using [`CFSocketSetSocketFlags(_:_:)`](cfsocketsetsocketflags(_:_:).md), the native socket associated with a CFSocket object is closed when the CFSocket object is invalidated. When disabled, the native socket remains open. This option is enabled by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfsocketautomaticallyreenabledatacallback)*