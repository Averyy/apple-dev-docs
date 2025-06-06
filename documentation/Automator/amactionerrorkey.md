# AMActionErrorKey

**Framework**: Automator  
**Kind**: var

A key to retrieve the action that caused an error.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
var AMActionErrorKey: String { get }
```

#### Discussion

Use this key to obtain, from the [`userInfo`](https://developer.apple.com/documentation/foundation/nserror/1411580-userinfo) dictionary of an instance of [`NSError`](https://developer.apple.com/documentation/Foundation/NSError), a reference to the action ([`AMAction`](amaction.md)) that caused the error.

## See Also

- [var AMAutomatorErrorDomain: String](amautomatorerrordomain.md)
  A string that identifies the Automator error domain.
- [struct AMError](amerror.md)
  An Automator error.
- [AMError.Code](amerror/code.md)
  Automator error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amactionerrorkey)*