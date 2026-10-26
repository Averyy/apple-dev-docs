# ABImageClientCallback

**Framework**: Address Book  
**Kind**: typealias  
**Role**: Type Alias

Prototype of a callback function used to notify an application when an asynchronous image fetch is complete.

**Availability**:
- macOS

## Declaration

```swift
typealias ABImageClientCallback = (CFData?, CFIndex, UnsafeMutableRawPointer?) -> Void
```

```c
typedef void (*)(const struct __CFData *, long, void *) ABImageClientCallback;
```

#### Discussion

Use the [`ABBeginLoadingImageDataForClient(_:_:_:)`](./abbeginloadingimagedataforclient%28_,_,_%29.md) function to begin an asynchronous fetch, and the [`ABCancelLoadingImageDataForTag(_:)`](./abcancelloadingimagedatafortag%28_%29.md) function to cancel an asynchronous fetch.

## Parameters

- `imageData`: The image data in Quicktime compatible format that was loaded from an asynchronous fetch. `NULL` if the fetch failed.
- `tag`: The tracking number for this fetch that should have been obtained from a previous call to the [`ABBeginLoadingImageDataForClient(_:_:_:)`](./abbeginloadingimagedataforclient%28_,_,_%29.md) function.
- `info`: An untyped pointer to program-defined data that was passed to the [`ABBeginLoadingImageDataForClient(_:_:_:)`](./abbeginloadingimagedataforclient%28_,_,_%29.md) function.

## See Also

### Callbacks
- [ABActionCopyTitleCallback](./abactioncopytitlecallback.md)
  The title of the menu item for the action.
- [ABActionEnabledCallback](./abactionenabledcallback.md)
  Return `true` ifthe action menu item should be enabled, `false` otherwise.If the property returned by `ABActionGetPropertyCallback` isa multi-value property, `identifier` contains theunique identifier of the value selected.
- [ABActionGetPropertyCallback](./abactiongetpropertycallback.md)
  Return the property the action applies to.
- [ABActionSelectedCallback](./abactionselectedcallback.md)
  Execute the action. If the property returnedby [`ABActionGetPropertyCallback`](./abactiongetpropertycallback.md) isa multi-value property, `identifier` containsthe unique identifier of the value selected; otherwise, identifieris `NULL`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abimageclientcallback)*