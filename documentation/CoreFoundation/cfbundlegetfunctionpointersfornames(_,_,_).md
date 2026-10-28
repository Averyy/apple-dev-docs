# CFBundleGetFunctionPointersForNames(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Constructs a function table containing pointers to all of the functions found in a bundle’s main executable code.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func CFBundleGetFunctionPointersForNames(_ bundle: CFBundle!, _ functionNames: CFArray!, _ ftbl: UnsafeMutablePointer<UnsafeMutableRawPointer?>!)
```

```c
extern void CFBundleGetFunctionPointersForNames(CFBundleRef bundle, CFArrayRef functionNames, void * ftbl[]);
```

## Discussion

Calling this function causes the bundle’s code to be loaded if necessary.

## Parameters

- `bundle`: The bundle to examine.
- `functionNames`: A CFArray object containing a list of the function names to locate.
- `ftbl`: A C array into which this function stores the function pointers for the symbols specified in `functionNames`. The array contains `NULL` for any names in `functionNames` that cannot be found.

## See Also

### Managing Executable Code
- [func CFBundleGetDataPointerForName(CFBundle!, CFString!) -> UnsafeMutableRawPointer!](./cfbundlegetdatapointerforname%28_,_%29.md)
  Returns a data pointer to a symbol of the given name.
- [func CFBundleGetDataPointersForNames(CFBundle!, CFArray!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](./cfbundlegetdatapointersfornames%28_,_,_%29.md)
  Returns a C array of data pointer to symbols of the given names.
- [func CFBundleGetFunctionPointerForName(CFBundle!, CFString!) -> UnsafeMutableRawPointer!](./cfbundlegetfunctionpointerforname%28_,_%29.md)
  Returns a pointer to a function in a bundle’s executable code using the function name as the search key.
- [func CFBundleGetPlugIn(CFBundle!) -> CFPlugIn!](./cfbundlegetplugin%28_%29.md)
  Returns a bundle’s plug-in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlegetfunctionpointersfornames(_:_:_:))*