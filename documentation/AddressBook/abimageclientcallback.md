# ABImageClientCallback

**Framework**: Address Book  
**Kind**: typealias

Prototype of a callback function used to notify an application when an asynchronous image fetch is complete.

**Availability**:
- macOS ?+

## Declaration

```swift
typealias ABImageClientCallback = (CFData?, CFIndex, UnsafeMutableRawPointer?) -> Void
```

#### Discussion

Use the [`ABBeginLoadingImageDataForClient(_:_:_:)`](abbeginloadingimagedataforclient(_:_:_:).md) function to begin an asynchronous fetch, and the [`ABCancelLoadingImageDataForTag(_:)`](abcancelloadingimagedatafortag(_:).md) function to cancel an asynchronous fetch.

## Parameters

- `imageData`: The image data in Quicktime compatible format that was loaded from an asynchronous fetch.   if the fetch failed.
- `tag`: The tracking number for this fetch that should have been obtained from a previous call to the   function.
- `info`: An untyped pointer to program-defined data that was passed to the   function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abimageclientcallback)*