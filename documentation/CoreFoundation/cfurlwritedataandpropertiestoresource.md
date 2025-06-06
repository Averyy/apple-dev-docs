# CFURLWriteDataAndPropertiesToResource(_:_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Writes the given data and properties to a given URL.

**Availability**:
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFURLWriteDataAndPropertiesToResource(_ url: CFURL!, _ dataToWrite: CFData!, _ propertiesToWrite: CFDictionary!, _ errorCode: UnsafeMutablePointer<Int32>!) -> Bool
```

#### Return Value

`true` if successful, `false` otherwise.

#### Discussion

Properties not present in `propertiesToWrite` are left unchanged, hence if `propertiesToWrite` is `NULL` or empty, the URL’s properties are not changed at all.

If `url` uses a file scheme and it references a file, the contents of `dataToWrite` are written to the referenced file, overwriting any preexisting data, and the file’s properties are modified according to `propertiesToWrite`. If the file does not exist, but all intermediate directories along the path do already exist, the file is created (otherwise it is not).

If `url` uses a file scheme and it references a directory (the last path character is “`/`”), the contents of `dataToWrite` are ignored, but if the parameter value is not `NULL`—and all intermediate directories along the path do already exist—a new directory is created  (otherwise it is not).

If `url` uses an http scheme, an http `PUT` request is sent to the resource with `propertiesToWrite` as the header fields and `dataToWrite` as the data.

## Parameters

- `url`: The resource to write.
- `dataToWrite`: The data to write. Pass   to write only properties.
- `propertiesToWrite`: The properties to write. Pass   to write only data. See   and   for the list of available properties.
- `errorCode`: Upon return,   if successful, otherwise contains an error code indicating the nature of the problem. See   for a list of possible error codes.

## See Also

- [func CFURLCreateDataAndPropertiesFromResource(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFData>?>!, UnsafeMutablePointer<Unmanaged<CFDictionary>?>!, CFArray!, UnsafeMutablePointer<Int32>!) -> Bool](cfurlcreatedataandpropertiesfromresource(_:_:_:_:_:_:).md)
  Loads the data and properties referred to by a given URL.
- [func CFURLCreatePropertyFromResource(CFAllocator!, CFURL!, CFString!, UnsafeMutablePointer<Int32>!) -> CFTypeRef!](cfurlcreatepropertyfromresource(_:_:_:_:).md)
  Returns a given property specified by a given URL and property string.
- [func CFURLDestroyResource(CFURL!, UnsafeMutablePointer<Int32>!) -> Bool](cfurldestroyresource(_:_:).md)
  Destroys a resource indicated by a given URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfurlwritedataandpropertiestoresource(_:_:_:_:))*