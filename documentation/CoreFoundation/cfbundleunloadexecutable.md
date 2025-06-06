# CFBundleUnloadExecutable(_:)

**Framework**: Core Foundation  
**Kind**: func

Unloads the main executable for the specified bundle.

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
func CFBundleUnloadExecutable(_ bundle: CFBundle!)
```

#### Discussion

You should typically try to avoid using this function, but instead use [`CFBundleGetFunctionPointerForName(_:_:)`](cfbundlegetfunctionpointerforname(_:_:).md) and related functions since these make management of the bundle easier (when the last reference to the CFBundle object is released, and it is finally deallocated, then the code will be unloaded if it is still loaded, and if the executable is of a type that supports unloading).

## Parameters

- `bundle`: The bundle whose main executable you want to unload.

## See Also

- [func CFBundleIsExecutableLoaded(CFBundle!) -> Bool](cfbundleisexecutableloaded(_:).md)
  Obtains information about the load status for a bundle’s main executable.
- [func CFBundlePreflightExecutable(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfbundlepreflightexecutable(_:_:).md)
  Returns a Boolean value that indicates whether a given bundle is loaded or appears to be loadable.
- [func CFBundleLoadExecutable(CFBundle!) -> Bool](cfbundleloadexecutable(_:).md)
  Loads a bundle’s main executable code into memory and dynamically links it into the running application.
- [func CFBundleLoadExecutableAndReturnError(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfbundleloadexecutableandreturnerror(_:_:).md)
  Returns a Boolean value that indicates whether a given bundle is loaded, attempting to load it if necessary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundleunloadexecutable(_:))*