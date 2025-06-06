# CFBundleLoadExecutableAndReturnError(_:_:)

**Framework**: Core Foundation  
**Kind**: func

Returns a Boolean value that indicates whether a given bundle is loaded, attempting to load it if necessary.

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
func CFBundleLoadExecutableAndReturnError(_ bundle: CFBundle!, _ error: UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool
```

#### Return Value

If `bundle` is already loaded, returns `true`. If `bundle` is not already loaded, attempts to load `bundle`; if that attempt succeeds returns `true`, otherwise returns `false`.

## Parameters

- `bundle`: The bundle to examine.
- `error`: Upon return, if an error occurs contains a CFError that describes the problem. Ownership follows the  .

## See Also

- [func CFBundleIsExecutableLoaded(CFBundle!) -> Bool](cfbundleisexecutableloaded(_:).md)
  Obtains information about the load status for a bundle’s main executable.
- [func CFBundlePreflightExecutable(CFBundle!, UnsafeMutablePointer<Unmanaged<CFError>?>!) -> Bool](cfbundlepreflightexecutable(_:_:).md)
  Returns a Boolean value that indicates whether a given bundle is loaded or appears to be loadable.
- [func CFBundleLoadExecutable(CFBundle!) -> Bool](cfbundleloadexecutable(_:).md)
  Loads a bundle’s main executable code into memory and dynamically links it into the running application.
- [func CFBundleUnloadExecutable(CFBundle!)](cfbundleunloadexecutable(_:).md)
  Unloads the main executable for the specified bundle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corefoundation/cfbundleloadexecutableandreturnerror(_:_:))*