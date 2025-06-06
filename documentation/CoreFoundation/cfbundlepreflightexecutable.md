# CFBundlePreflightExecutable(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a Boolean value that indicates whether a given bundle is loaded or appears to be loadable.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CFBundlePreflightExecutable(_ bundle: CFBundle!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

#### Return Value

`true` if `bundle` is loaded or upon inspection appears to be loadable, otherwise `false`.

#### Discussion

If this function returns true, this does not mean that the bundle is definitively loadable, since it may fail to load due to link errors or other problems not readily detectable.

## Parameters

- `bundle`: The bundle to examine.
- `error`: Upon return, if an error occurs contains a CFError that describes the problem. Ownership follows the  .

## See Also

- [func CFBundleIsExecutableLoaded(CFBundle!) -> Bool](cfbundleisexecutableloaded(_:).md)
  Obtains information about the load status for a bundle’s main executable.
- [func CFBundleLoadExecutable(CFBundle!) -> Bool](cfbundleloadexecutable(_:).md)
  Loads a bundle’s main executable code into memory and dynamically links it into the running application.
- [func CFBundleLoadExecutableAndReturnError(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfbundleloadexecutableandreturnerror(_:_:).md)
  Returns a Boolean value that indicates whether a given bundle is loaded, attempting to load it if necessary.
- [func CFBundleUnloadExecutable(CFBundle!)](cfbundleunloadexecutable(_:).md)
  Unloads the main executable for the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundlepreflightexecutable(_:_:))*