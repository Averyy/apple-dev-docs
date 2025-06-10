# ABCancelLoadingImageDataForTag(_:)

**Framework**: Address Book  
**Kind**: func

Cancels an asynchronous fetch of an image for the given tag.

**Availability**:
- macOS ?+

## Declaration

```swift
func ABCancelLoadingImageDataForTag(_ tag: CFIndex)
```

#### Discussion

Use the [`ABBeginLoadingImageDataForClient(_:_:_:)`](abbeginloadingimagedataforclient(_:_:_:).md) function to begin an asynchronous fetch. Implement your callback function to receive the fetched image. Use this function to cancel an asynchronous fetch.

## Parameters

- `tag`: Used to track an asynchronous fetch. This parameter should have been returned from a previous call to the   function.

## See Also

- [func ABBeginLoadingImageDataForClient(ABPersonRef!, ABImageClientCallback!, UnsafeMutableRawPointer!) -> CFIndex](abbeginloadingimagedataforclient(_:_:_:).md)
  Starts an asynchronous fetch for image data in all locations, and returns a non-zero tag for tracking.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abcancelloadingimagedatafortag(_:))*