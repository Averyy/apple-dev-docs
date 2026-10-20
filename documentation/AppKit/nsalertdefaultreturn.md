# NSAlertDefaultReturn

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The user pressed the default button.

**Availability**:
- macOS 10.0+ - Deprecated in 10.10

> **Deprecated**: `NSRunAlertPanel` and `NSGetAlertPanel` are deprecated; use [`NSAlert`](./nsalert.md) APIs instead.

## Declaration

```swift
var NSAlertDefaultReturn: Int { get }
```

```c
NSAlertDefaultReturn
```

## See Also

### Deprecated
- [var NSAlertAlternateReturn: Int](./nsalertalternatereturn.md)
  The user pressed the alternate button.
- [var NSAlertOtherReturn: Int](./nsalertotherreturn.md)
  The user pressed a second alternate button.
- [var NSAlertErrorReturn: Int](./nsalerterrorreturn.md)
  The alert cannot identify the reason it was closed; it may have been closed by an external source or by a button other than those listed above.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalertdefaultreturn)*