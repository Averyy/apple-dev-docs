# CFBundleLoadExecutable(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Loads a bundle’s main executable code into memory and dynamically links it into the running application.

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
func CFBundleLoadExecutable(_ bundle: CFBundle!) -> Bool
```

```c
extern Boolean CFBundleLoadExecutable(CFBundleRef bundle);
```

## Return Value

`true` if the executable was successfully loaded, otherwise `false`.

## Discussion

You should typically try to avoid using this function, but instead use [`CFBundleGetFunctionPointerForName(_:_:)`](./cfbundlegetfunctionpointerforname%28_,_%29.md) and related functions since these make memory management of the bundle easier.

## Parameters

- `bundle`: The bundle whose main executable you want to load.

## See Also

### Loading and Unloading a Bundle
- [func CFBundleIsExecutableLoaded(CFBundle!) -> Bool](./cfbundleisexecutableloaded%28_%29.md)
  Obtains information about the load status for a bundle’s main executable.
- [func CFBundlePreflightExecutable(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfbundlepreflightexecutable%28_,_%29.md)
  Returns a Boolean value that indicates whether a given bundle is loaded or appears to be loadable.
- [func CFBundleLoadExecutableAndReturnError(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfbundleloadexecutableandreturnerror%28_,_%29.md)
  Returns a Boolean value that indicates whether a given bundle is loaded, attempting to load it if necessary.
- [func CFBundleUnloadExecutable(CFBundle!)](./cfbundleunloadexecutable%28_%29.md)
  Unloads the main executable for the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundleloadexecutable(_:))*