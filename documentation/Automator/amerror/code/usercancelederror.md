# AMError.Code.userCanceledError

**Framework**: Automator  
**Kind**: case  
**Role**: Case

An error that indicates the user cancelled.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
case userCanceledError
```

```c
AMUserCanceledError
```

## Discussion

This error is the same as the AppleScript error [`userCanceledErr`](../../../kernel/api-1645157-anonymous/usercancelederr.md). When an Apple Event is canceled by the user, a running action may return this error. Automator ignores the error and stops the workflow gracefully, without displaying the error to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amerror/code/usercancelederror)*