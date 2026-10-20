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


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abimageclientcallback)*