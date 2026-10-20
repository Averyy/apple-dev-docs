# kCFSocketCloseOnInvalidate

**Framework**: Core Foundation  
**Kind**: var  
**Role**: Global Variable

When enabled using [`CFSocketSetSocketFlags(_:_:)`](./cfsocketsetsocketflags%28_,_%29.md), the native socket associated with a CFSocket object is closed when the CFSocket object is invalidated. When disabled, the native socket remains open. This option is enabled by default.

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
var kCFSocketCloseOnInvalidate: CFOptionFlags { get }
```

```c
kCFSocketCloseOnInvalidate
```

## See Also

### Constants
- [var kCFSocketAutomaticallyReenableReadCallBack: CFOptionFlags](./kcfsocketautomaticallyreenablereadcallback.md)
- [var kCFSocketAutomaticallyReenableAcceptCallBack: CFOptionFlags](./kcfsocketautomaticallyreenableacceptcallback.md)
- [var kCFSocketAutomaticallyReenableDataCallBack: CFOptionFlags](./kcfsocketautomaticallyreenabledatacallback.md)
- [var kCFSocketAutomaticallyReenableWriteCallBack: CFOptionFlags](./kcfsocketautomaticallyreenablewritecallback.md)
- [var kCFSocketLeaveErrors: CFOptionFlags](./kcfsocketleaveerrors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfsocketcloseoninvalidate)*