# CFBundleIsExecutableLoaded(_:)

**Framework**: Core Foundation  
**Kind**: func  
**Role**: Function

Obtains information about the load status for a bundle’s main executable.

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
func CFBundleIsExecutableLoaded(_ bundle: CFBundle!) -> Bool
```

```c
extern Boolean CFBundleIsExecutableLoaded(CFBundleRef bundle);
```

## Return Value

`true` if `bundle`’s main executable has been loaded, otherwise `false`.

## Parameters

- `bundle`: The bundle to examine.

## See Also

### Loading and Unloading a Bundle
- [func CFBundlePreflightExecutable(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfbundlepreflightexecutable%28_,_%29.md)
  Returns a Boolean value that indicates whether a given bundle is loaded or appears to be loadable.
- [func CFBundleLoadExecutable(CFBundle!) -> Bool](./cfbundleloadexecutable%28_%29.md)
  Loads a bundle’s main executable code into memory and dynamically links it into the running application.
- [func CFBundleLoadExecutableAndReturnError(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](./cfbundleloadexecutableandreturnerror%28_,_%29.md)
  Returns a Boolean value that indicates whether a given bundle is loaded, attempting to load it if necessary.
- [func CFBundleUnloadExecutable(CFBundle!)](./cfbundleunloadexecutable%28_%29.md)
  Unloads the main executable for the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundleisexecutableloaded(_:))*