# Core Foundation URL Access Utilities

**Framework**: Core Foundation

#### Overview

Core Foundation URL Access Utilities give you convenient system-independent methods of creating, reading, updating, or deleting a URL resource.

Given a [`CFURL`](cfurl.md) object that holds either a file or http URL, you can read the resource’s data with the [`CFURLCreateDataAndPropertiesFromResource(_:_:_:_:_:_:)`](cfurlcreatedataandpropertiesfromresource(_:_:_:_:_:_:).md) function. You can write data to the URL resource, possibly creating a new file, with the [`CFURLWriteDataAndPropertiesToResource(_:_:_:_:)`](cfurlwritedataandpropertiestoresource(_:_:_:_:).md) function. Finally, you can destroy, or delete, the resource pointed to by the URL with the [`CFURLDestroyResource(_:_:)`](cfurldestroyresource(_:_:).md) function.

## Topics

### Core Foundation URL Access Utilities Miscellaneous Functions
- [func CFURLCreateDataAndPropertiesFromResource(CFAllocator!, CFURL!, UnsafeMutablePointer<Unmanaged<CFData>?>!, UnsafeMutablePointer<Unmanaged<CFDictionary>?>!, CFArray!, UnsafeMutablePointer<Int32>!) -> Bool](cfurlcreatedataandpropertiesfromresource(_:_:_:_:_:_:).md)
  Loads the data and properties referred to by a given URL.
- [func CFURLCreatePropertyFromResource(CFAllocator!, CFURL!, CFString!, UnsafeMutablePointer<Int32>!) -> CFTypeRef!](cfurlcreatepropertyfromresource(_:_:_:_:).md)
  Returns a given property specified by a given URL and property string.
- [func CFURLDestroyResource(CFURL!, UnsafeMutablePointer<Int32>!) -> Bool](cfurldestroyresource(_:_:).md)
  Destroys a resource indicated by a given URL.
- [func CFURLWriteDataAndPropertiesToResource(CFURL!, CFData!, CFDictionary!, UnsafeMutablePointer<Int32>!) -> Bool](cfurlwritedataandpropertiestoresource(_:_:_:_:).md)
  Writes the given data and properties to a given URL.
### Constants
- [enum CFURLError](cfurlerror.md)
  `CFURL` error codes.
- [File URL Properties](file-url-properties.md)
  Properties for file URL resources.
- [HTTP URL Properties](http-url-properties.md)
  Properties for HTTP URL resources.

## See Also

- [Base Utilities](base-utilities.md)
- [Byte-Order Utilities](byte-order-utilities.md)
- [Preferences Utilities](preferences-utilities.md)
- [Socket Name Server Utilities](socket-name-server-utilities.md)
- [Time Utilities](time-utilities.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/core-foundation-url-access-utilities)*