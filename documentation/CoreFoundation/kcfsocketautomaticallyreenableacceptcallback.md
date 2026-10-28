# kCFSocketAutomaticallyReenableAcceptCallBack

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
var kCFSocketAutomaticallyReenableAcceptCallBack: CFOptionFlags { get }
```

```c
kCFSocketAutomaticallyReenableAcceptCallBack
```

## Discussion

When enabled using [`CFSocketSetSocketFlags(_:_:)`](./cfsocketsetsocketflags%28_,_%29.md), the accept callback is called every time someone connects to your socket. When disabled, the accept callback is called only once the next time a new socket connection is accepted. The accept callback is automatically reenabled by default.

## See Also

### Constants
- [var kCFSocketAutomaticallyReenableReadCallBack: CFOptionFlags](./kcfsocketautomaticallyreenablereadcallback.md)
- [var kCFSocketAutomaticallyReenableDataCallBack: CFOptionFlags](./kcfsocketautomaticallyreenabledatacallback.md)
- [var kCFSocketAutomaticallyReenableWriteCallBack: CFOptionFlags](./kcfsocketautomaticallyreenablewritecallback.md)
- [var kCFSocketLeaveErrors: CFOptionFlags](./kcfsocketleaveerrors.md)
- [var kCFSocketCloseOnInvalidate: CFOptionFlags](./kcfsocketcloseoninvalidate.md)
  When enabled using [`CFSocketSetSocketFlags(_:_:)`](./cfsocketsetsocketflags%28_,_%29.md), the native socket associated with a CFSocket object is closed when the CFSocket object is invalidated. When disabled, the native socket remains open. This option is enabled by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfsocketautomaticallyreenableacceptcallback)*