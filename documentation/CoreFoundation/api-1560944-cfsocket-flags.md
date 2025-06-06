# CFSocket Flags

**Framework**: Core Foundation

Flags that can be set on a CFSocket object to control its behavior.

#### Overview

The flags for a CFSocket object are set with [`CFSocketSetSocketFlags(_:_:)`](cfsocketsetsocketflags(_:_:).md). To immediately enable or disable a callback, use [`CFSocketEnableCallBacks(_:_:)`](cfsocketenablecallbacks(_:_:).md) and [`CFSocketDisableCallBacks(_:_:)`](cfsocketdisablecallbacks(_:_:).md).

## Topics

### Constants
- [var kCFSocketAutomaticallyReenableReadCallBack: CFOptionFlags](kcfsocketautomaticallyreenablereadcallback.md)
- [var kCFSocketAutomaticallyReenableAcceptCallBack: CFOptionFlags](kcfsocketautomaticallyreenableacceptcallback.md)
- [var kCFSocketAutomaticallyReenableDataCallBack: CFOptionFlags](kcfsocketautomaticallyreenabledatacallback.md)
- [var kCFSocketAutomaticallyReenableWriteCallBack: CFOptionFlags](kcfsocketautomaticallyreenablewritecallback.md)
- [var kCFSocketLeaveErrors: CFOptionFlags](kcfsocketleaveerrors.md)
- [var kCFSocketCloseOnInvalidate: CFOptionFlags](kcfsocketcloseoninvalidate.md)
  When enabled using [`CFSocketSetSocketFlags(_:_:)`](cfsocketsetsocketflags(_:_:).md), the native socket associated with a CFSocket object is closed when the CFSocket object is invalidated. When disabled, the native socket remains open. This option is enabled by default.

## See Also

- [struct CFSocketCallBackType](cfsocketcallbacktype.md)
  Types of socket activity that can cause the callback function of a CFSocket object to be called.
- [enum CFSocketError](cfsocketerror.md)
  Error codes for many CFSocket functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/1560944-cfsocket-flags)*