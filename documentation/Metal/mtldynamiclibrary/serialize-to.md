# serialize(to:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Writes the contents of the dynamic library to a file.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func serialize(to url: URL) throws
```

#### Discussion

When the methods succeeds, the file contains a representation of the [`MTLLibrary`](mtllibrary.md) from the [`MTLDynamicLibrary`](mtldynamiclibrary.md) that creates it, as well as the binaries it has for the device your app is running on.

Such files may be combined with offline tools to contain the compiled code for multiple devices.

If this MTLDynamicLibrary was created from a file that contained compiled code for multiple devices, the compiled code for all other devices is not written (since only compiled code for the current device was loaded).

## Parameters

- `url`: The URL for the destination file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldynamiclibrary/serialize(to:))*