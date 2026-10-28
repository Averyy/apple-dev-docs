# kCFSocketAutomaticallyReenableWriteCallBack

**Framework**: Core Foundation  
**Kind**: var  
**Role**: Global Variable

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var kCFSocketAutomaticallyReenableWriteCallBack: CFOptionFlags { get }
```

```c
kCFSocketAutomaticallyReenableWriteCallBack
```

## Discussion

When enabled using [`CFSocketSetSocketFlags(_:_:)`](./cfsocketsetsocketflags%28_,_%29.md), the write callback is called every time more data can be written to the socket. When disabled, the write callback is called only the next time data can be written. The write callback is not automatically reenabled by default.

## See Also

### Constants
- [var kCFSocketAutomaticallyReenableReadCallBack: CFOptionFlags](./kcfsocketautomaticallyreenablereadcallback.md)
- [var kCFSocketAutomaticallyReenableAcceptCallBack: CFOptionFlags](./kcfsocketautomaticallyreenableacceptcallback.md)
- [var kCFSocketAutomaticallyReenableDataCallBack: CFOptionFlags](./kcfsocketautomaticallyreenabledatacallback.md)
- [var kCFSocketLeaveErrors: CFOptionFlags](./kcfsocketleaveerrors.md)
- [var kCFSocketCloseOnInvalidate: CFOptionFlags](./kcfsocketcloseoninvalidate.md)
  When enabled using [`CFSocketSetSocketFlags(_:_:)`](./cfsocketsetsocketflags%28_,_%29.md), the native socket associated with a CFSocket object is closed when the CFSocket object is invalidated. When disabled, the native socket remains open. This option is enabled by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfsocketautomaticallyreenablewritecallback)*