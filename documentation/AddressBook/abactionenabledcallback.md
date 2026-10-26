# ABActionEnabledCallback

**Framework**: Address Book  
**Kind**: typealias  
**Role**: Type Alias

Return `true` ifthe action menu item should be enabled, `false` otherwise.If the property returned by `ABActionGetPropertyCallback` isa multi-value property, `identifier` contains theunique identifier of the value selected.

**Availability**:
- macOS

## Declaration

```c
typedef unsigned char (*)(struct __ABPerson *, const struct __CFString *) ABActionEnabledCallback;
```

## See Also

### Callbacks
- [typealias ABImageClientCallback](./abimageclientcallback.md)
  Prototype of a callback function used to notify an application when an asynchronous image fetch is complete.
- [ABActionCopyTitleCallback](./abactioncopytitlecallback.md)
  The title of the menu item for the action.
- [ABActionGetPropertyCallback](./abactiongetpropertycallback.md)
  Return the property the action applies to.
- [ABActionSelectedCallback](./abactionselectedcallback.md)
  Execute the action. If the property returnedby [`ABActionGetPropertyCallback`](./abactiongetpropertycallback.md) isa multi-value property, `identifier` containsthe unique identifier of the value selected; otherwise, identifieris `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abactionenabledcallback)*