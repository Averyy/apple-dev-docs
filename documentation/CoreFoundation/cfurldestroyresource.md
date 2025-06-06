# CFURLDestroyResource(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Destroys a resource indicated by a given URL.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFURLDestroyResource(_ url: CFURL!, _ errorCode: UnsafeMutablePointer<Int32>!) -> Bool
```

#### Return Value

`true` if successful, `false` otherwise.

#### Discussion

If `url` uses an http scheme, an http `DELETE` request is sent to the resource. If `url` uses a file scheme, then:

- if the reference is a file, the file is deleted;
- if the reference is a directory and the directory is empty, the directory is deleted;
- if the reference is a directory and the directory is not empty, the function returns `false` and `errorCode` contains `kCFURLUnknownError`.

## Parameters

- `url`: The   object of the resource to destroy.
- `errorCode`: On return,   if successful, otherwise an error code indicating the nature of the problem. See   for a list of possible error codes.

## See Also

- [func CFURLCreateDataAndPropertiesFromResource(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFData>?>!, UnsafeMutablePointer<Unmanaged<CFDictionary>?>!, CFArray!, UnsafeMutablePointer<Int32>!) -> Bool](cfurlcreatedataandpropertiesfromresource(_:_:_:_:_:_:).md)
  Loads the data and properties referred to by a given URL.
- [func CFURLCreatePropertyFromResource(CFAllocator!, CFURL!, CFString!, UnsafeMutablePointer<Int32>!) -> CFTypeRef!](cfurlcreatepropertyfromresource(_:_:_:_:).md)
  Returns a given property specified by a given URL and property string.
- [func CFURLWriteDataAndPropertiesToResource(CFURL!, CFData!, CFDictionary!, UnsafeMutablePointer<Int32>!) -> Bool](cfurlwritedataandpropertiestoresource(_:_:_:_:).md)
  Writes the given data and properties to a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurldestroyresource(_:_:))*