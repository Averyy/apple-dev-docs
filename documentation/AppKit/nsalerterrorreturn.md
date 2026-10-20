# NSAlertErrorReturn

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The alert cannot identify the reason it was closed; it may have been closed by an external source or by a button other than those listed above.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use NSAlertFirstButtonReturn and other NSModalResponses with an NSAlert presentation instead

## Declaration

```swift
var NSAlertErrorReturn: Int { get }
```

```c
NSAlertErrorReturn
```

## See Also

### Deprecated
- [var NSAlertDefaultReturn: Int](./nsalertdefaultreturn.md)
  The user pressed the default button.
- [var NSAlertAlternateReturn: Int](./nsalertalternatereturn.md)
  The user pressed the alternate button.
- [var NSAlertOtherReturn: Int](./nsalertotherreturn.md)
  The user pressed a second alternate button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalerterrorreturn)*