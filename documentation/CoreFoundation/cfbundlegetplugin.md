# CFBundleGetPlugIn(_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a bundle’s plug-in.

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
func CFBundleGetPlugIn(_ bundle: CFBundle!) -> CFPlugIn!
```

#### Return Value

The plug-in for `bundle`. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `bundle`: The bundle to examine.

## See Also

- [func CFBundleGetDataPointerForName(CFBundle!, CFString!) -> UnsafeMutableRawPointer!](cfbundlegetdatapointerforname(_:_:).md)
  Returns a data pointer to a symbol of the given name.
- [func CFBundleGetDataPointersForNames(CFBundle!, CFArray!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](cfbundlegetdatapointersfornames(_:_:_:).md)
  Returns a C array of data pointer to symbols of the given names.
- [func CFBundleGetFunctionPointerForName(CFBundle!, CFString!) -> UnsafeMutableRawPointer!](cfbundlegetfunctionpointerforname(_:_:).md)
  Returns a pointer to a function in a bundle’s executable code using the function name as the search key.
- [func CFBundleGetFunctionPointersForNames(CFBundle!, CFArray!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](cfbundlegetfunctionpointersfornames(_:_:_:).md)
  Constructs a function table containing pointers to all of the functions found in a bundle’s main executable code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlegetplugin(_:))*