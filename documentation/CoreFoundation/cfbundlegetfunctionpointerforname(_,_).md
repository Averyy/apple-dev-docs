# CFBundleGetFunctionPointerForName(_:_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Returns a pointer to a function in a bundle’s executable code using the function name as the search key.

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
func CFBundleGetFunctionPointerForName(_ bundle: CFBundle!, _ functionName: CFString!) -> UnsafeMutableRawPointer!
```

```c
extern void *CFBundleGetFunctionPointerForName(CFBundleRef bundle, CFStringRef functionName);
```

## Return Value

A pointer to a function in a `bundle`’s executable code, or `NULL` if `functionName` cannot be found. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

Calling this function will cause the bundle’s code to be loaded if necessary.

## Parameters

- `bundle`: The bundle to examine.
- `functionName`: The name of the function to locate.

## See Also

### Managing Executable Code
- [func CFBundleGetDataPointerForName(CFBundle!, CFString!) -> UnsafeMutableRawPointer!](./cfbundlegetdatapointerforname%28_,_%29.md)
  Returns a data pointer to a symbol of the given name.
- [func CFBundleGetDataPointersForNames(CFBundle!, CFArray!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](./cfbundlegetdatapointersfornames%28_,_,_%29.md)
  Returns a C array of data pointer to symbols of the given names.
- [func CFBundleGetFunctionPointersForNames(CFBundle!, CFArray!, UnsafeMutablePointer<UnsafeMutableRawPointer?>!)](./cfbundlegetfunctionpointersfornames%28_,_,_%29.md)
  Constructs a function table containing pointers to all of the functions found in a bundle’s main executable code.
- [func CFBundleGetPlugIn(CFBundle!) -> CFPlugIn!](./cfbundlegetplugin%28_%29.md)
  Returns a bundle’s plug-in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlegetfunctionpointerforname(_:_:))*