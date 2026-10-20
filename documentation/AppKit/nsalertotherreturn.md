# NSAlertOtherReturn

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The user pressed a second alternate button.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: Use NSAlertFirstButtonReturn and other NSModalResponses with an NSAlert presentation instead

## Declaration

```swift
var NSAlertOtherReturn: Int { get }
```

```c
NSAlertOtherReturn
```

## See Also

### Deprecated
- [var NSAlertDefaultReturn: Int](./nsalertdefaultreturn.md)
  The user pressed the default button.
- [var NSAlertAlternateReturn: Int](./nsalertalternatereturn.md)
  The user pressed the alternate button.
- [var NSAlertErrorReturn: Int](./nsalerterrorreturn.md)
  The alert cannot identify the reason it was closed; it may have been closed by an external source or by a button other than those listed above.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalertotherreturn)*