# CFBundleGetDataPointerForName(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a data pointer to a symbol of the given name.

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
func CFBundleGetDataPointerForName(_ bundle: CFBundle!, _ symbolName: CFString!) -> UnsafeMutableRawPointer!
```

#### Return Value

A data pointer to a symbol named `symbolName` in `bundle`, or `NULL` if `symbolName` cannot be found. Ownership follows the [`The Get Rule`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Parameters

- `bundle`: The bundle to examine.
- `symbolName`: The name of the symbol you are searching for.

## See Also

- [func CFBundleGetDataPointersForNames(CFBundle!, CFArray!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](cfbundlegetdatapointersfornames(_:_:_:).md)
  Returns a C array of data pointer to symbols of the given names.
- [func CFBundleGetFunctionPointerForName(CFBundle!, CFString!) -> UnsafeMutableRawPointer!](cfbundlegetfunctionpointerforname(_:_:).md)
  Returns a pointer to a function in a bundle’s executable code using the function name as the search key.
- [func CFBundleGetFunctionPointersForNames(CFBundle!, CFArray!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](cfbundlegetfunctionpointersfornames(_:_:_:).md)
  Constructs a function table containing pointers to all of the functions found in a bundle’s main executable code.
- [func CFBundleGetPlugIn(CFBundle!) -> CFPlugIn!](cfbundlegetplugin(_:).md)
  Returns a bundle’s plug-in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlegetdatapointerforname(_:_:))*