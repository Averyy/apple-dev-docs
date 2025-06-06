# CFBundleLoadExecutable(_:)

**Framework**: Core Foundation  
**Kind**: func

Loads a bundle’s main executable code into memory and dynamically links it into the running application.

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
func CFBundleLoadExecutable(_ bundle: CFBundle!) -> Bool
```

#### Return Value

`true` if the executable was successfully loaded, otherwise `false`.

#### Discussion

You should typically try to avoid using this function, but instead use [`CFBundleGetFunctionPointerForName(_:_:)`](cfbundlegetfunctionpointerforname(_:_:).md) and related functions since these make memory management of the bundle easier.

## Parameters

- `bundle`: The bundle whose main executable you want to load.

## See Also

- [func CFBundleIsExecutableLoaded(CFBundle!) -> Bool](cfbundleisexecutableloaded(_:).md)
  Obtains information about the load status for a bundle’s main executable.
- [func CFBundlePreflightExecutable(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfbundlepreflightexecutable(_:_:).md)
  Returns a Boolean value that indicates whether a given bundle is loaded or appears to be loadable.
- [func CFBundleLoadExecutableAndReturnError(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfbundleloadexecutableandreturnerror(_:_:).md)
  Returns a Boolean value that indicates whether a given bundle is loaded, attempting to load it if necessary.
- [func CFBundleUnloadExecutable(CFBundle!)](cfbundleunloadexecutable(_:).md)
  Unloads the main executable for the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundleloadexecutable(_:))*