# consumeImageData(_:forTag:)

**Framework**: Address Book  
**Kind**: method  
**Required**: Yes

Gets the image data for the given tag that was initiated by an asynchronous fetch.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func consumeImageData(_ data: Data!, forTag tag: Int)
```

#### Discussion

In the case of a multithreaded application, this method is always called on the main thread.

## Parameters

- `data`: You can use this image data with the   method of the   class.
- `tag`: The tag returned from a previous call to the     method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/addressbook/abimageclient/consumeimagedata(_:fortag:))*