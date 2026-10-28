# ABBeginLoadingImageDataForClient(_:_:_:)

**Framework**: Address Book  
**Kind**: func  
**Role**: Function

Starts an asynchronous fetch for image data in all locations, and returns a non-zero tag for tracking.

**Availability**:
- macOS

## Declaration

```swift
func ABBeginLoadingImageDataForClient(_ person: ABPersonRef!, _ callback: ABImageClientCallback!, _ refcon: UnsafeMutableRawPointer!) -> CFIndex
```

```c
extern CFIndex ABBeginLoadingImageDataForClient(ABPersonRef person, ABImageClientCallback callback, void *refcon);
```

## Return Value

A non-zero tag for tracking

## Discussion

Use this function to begin an asynchronous fetch. Implement your callback function to receive the fetched image. Use the [`ABCancelLoadingImageDataForTag(_:)`](./abcancelloadingimagedatafortag%28_%29.md) function to cancel an asynchronous fetch.

## Parameters

- `person`: The person whose image data you wish to fetch.
- `callback`: The function to call when the fetch is completed.
- `refcon`: An untyped pointer to program-defined data that will be passed to the callback.

## See Also

### Images
- [func ABCancelLoadingImageDataForTag(CFIndex)](./abcancelloadingimagedatafortag%28_%29.md)
  Cancels an asynchronous fetch of an image for the given tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abbeginloadingimagedataforclient(_:_:_:))*