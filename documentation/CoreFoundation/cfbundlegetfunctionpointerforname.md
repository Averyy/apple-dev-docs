# CFBundleGetFunctionPointerForName(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a pointer to a function in a bundle’s executable code using the function name as the search key.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func CFBundleGetFunctionPointerForName(_ bundle: CFBundle!, _ functionName: CFString!) -> UnsafeMutableRawPointer!
```

#### Return Value

A pointer to a function in a `bundle`’s executable code, or `NULL` if `functionName` cannot be found. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

#### Discussion

Calling this function will cause the bundle’s code to be loaded if necessary.

## Parameters

- `bundle`: The bundle to examine.
- `functionName`: The name of the function to locate.

## See Also

- [func CFBundleGetDataPointerForName(CFBundle!, CFString!) -> UnsafeMutableRawPointer!](cfbundlegetdatapointerforname(_:_:).md)
  Returns a data pointer to a symbol of the given name.
- [func CFBundleGetDataPointersForNames(CFBundle!, CFArray!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](cfbundlegetdatapointersfornames(_:_:_:).md)
  Returns a C array of data pointer to symbols of the given names.
- [func CFBundleGetFunctionPointersForNames(CFBundle!, CFArray!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](cfbundlegetfunctionpointersfornames(_:_:_:).md)
  Constructs a function table containing pointers to all of the functions found in a bundle’s main executable code.
- [func CFBundleGetPlugIn(CFBundle!) -> CFPlugIn!](cfbundlegetplugin(_:).md)
  Returns a bundle’s plug-in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlegetfunctionpointerforname(_:_:))*