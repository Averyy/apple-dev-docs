# CFBundleGetDataPointersForNames(_:_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a C array of data pointer to symbols of the given names.

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
func CFBundleGetDataPointersForNames(_ bundle: CFBundle!, _ symbolNames: CFArray!, _ stbl: UnsafeMutablePointer<UnsafeMutableRawPointer?>!)
```

## Parameters

- `bundle`: The bundle to examine.
- `symbolNames`: A CFArray object containing CFString objects representing the symbol names to search for.
- `stbl`: A C array into which this function stores the data pointers for the symbols specified in  . The array contains   for any names in   that cannot be found.

## See Also

- [func CFBundleGetDataPointerForName(CFBundle!, CFString!) -> UnsafeMutableRawPointer!](cfbundlegetdatapointerforname(_:_:).md)
  Returns a data pointer to a symbol of the given name.
- [func CFBundleGetFunctionPointerForName(CFBundle!, CFString!) -> UnsafeMutableRawPointer!](cfbundlegetfunctionpointerforname(_:_:).md)
  Returns a pointer to a function in a bundle’s executable code using the function name as the search key.
- [func CFBundleGetFunctionPointersForNames(CFBundle!, CFArray!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](cfbundlegetfunctionpointersfornames(_:_:_:).md)
  Constructs a function table containing pointers to all of the functions found in a bundle’s main executable code.
- [func CFBundleGetPlugIn(CFBundle!) -> CFPlugIn!](cfbundlegetplugin(_:).md)
  Returns a bundle’s plug-in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlegetdatapointersfornames(_:_:_:))*