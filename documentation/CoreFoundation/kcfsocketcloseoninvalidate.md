# kCFSocketCloseOnInvalidate

**Framework**: Core Foundation  
**Kind**: var

When enabled using [`CFSocketSetSocketFlags(_:_:)`](cfsocketsetsocketflags(_:_:).md), the native socket associated with a CFSocket object is closed when the CFSocket object is invalidated. When disabled, the native socket remains open. This option is enabled by default.

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
var kCFSocketCloseOnInvalidate: CFOptionFlags { get }
```

## See Also

- [var kCFSocketAutomaticallyReenableReadCallBack: CFOptionFlags](kcfsocketautomaticallyreenablereadcallback.md)
- [var kCFSocketAutomaticallyReenableAcceptCallBack: CFOptionFlags](kcfsocketautomaticallyreenableacceptcallback.md)
- [var kCFSocketAutomaticallyReenableDataCallBack: CFOptionFlags](kcfsocketautomaticallyreenabledatacallback.md)
- [var kCFSocketAutomaticallyReenableWriteCallBack: CFOptionFlags](kcfsocketautomaticallyreenablewritecallback.md)
- [var kCFSocketLeaveErrors: CFOptionFlags](kcfsocketleaveerrors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/kcfsocketcloseoninvalidate)*