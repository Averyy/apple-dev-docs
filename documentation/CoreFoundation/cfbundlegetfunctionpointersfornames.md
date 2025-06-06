# CFBundleGetFunctionPointersForNames(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Constructs a function table containing pointers to all of the functions found in a bundle’s main executable code.

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
func CFBundleGetFunctionPointersForNames(_ bundle: CFBundle!, _ functionNames: CFArray!, _ ftbl: UnsafeMutablePointer<UnsafeMutableRawPointer?>!)
```

#### Discussion

Calling this function causes the bundle’s code to be loaded if necessary.

## Parameters

- `bundle`: The bundle to examine.
- `functionNames`: A CFArray object containing a list of the function names to locate.
- `ftbl`: A C array into which this function stores the function pointers for the symbols specified in  . The array contains   for any names in   that cannot be found.

## See Also

- [func CFBundleGetDataPointerForName(CFBundle!, CFString!) -> UnsafeMutableRawPointer!](cfbundlegetdatapointerforname(_:_:).md)
  Returns a data pointer to a symbol of the given name.
- [func CFBundleGetDataPointersForNames(CFBundle!, CFArray!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](cfbundlegetdatapointersfornames(_:_:_:).md)
  Returns a C array of data pointer to symbols of the given names.
- [func CFBundleGetFunctionPointerForName(CFBundle!, CFString!) -> UnsafeMutableRawPointer!](cfbundlegetfunctionpointerforname(_:_:).md)
  Returns a pointer to a function in a bundle’s executable code using the function name as the search key.
- [func CFBundleGetPlugIn(CFBundle!) -> CFPlugIn!](cfbundlegetplugin(_:).md)
  Returns a bundle’s plug-in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlegetfunctionpointersfornames(_:_:_:))*