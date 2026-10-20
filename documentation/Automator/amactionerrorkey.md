# AMActionErrorKey

**Framework**: Automator  
**Kind**: var  
**Role**: Global Variable

A key to retrieve the action that caused an error.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var AMActionErrorKey: String { get }
```

```c
#define AMActionErrorKey
```

#### Discussion

Use this key to obtain, from the [`userInfo`](../Foundation/nserror/userinfo.md) dictionary of an instance of [`NSError`](../Foundation/nserror.md), a reference to the action ([`AMAction`](./amaction.md)) that caused the error.

## See Also

### Errors
- [var AMAutomatorErrorDomain: String](./amautomatorerrordomain.md)
  A string that identifies the Automator error domain.
- [struct AMError](./amerror.md)
  An Automator error.
- [AMError.Code](./amerror/code.md)
  Automator error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amactionerrorkey)*