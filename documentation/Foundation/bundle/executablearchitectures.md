# executableArchitectures

**Framework**: Foundation  
**Kind**: property

An array of numbers indicating the architecture types supported by the bundle’s executable.

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
var executableArchitectures: [NSNumber]? { get }
```

#### Discussion

An array of `NSNumber` objects, each of which contains an integer value corresponding to a supported processor architecture. For a list of common architecture types, see the constants in [`Mach-O Architecture`](1495005-mach-o-architecture.md). If the bundle does not contain a Mach-O executable, this is `nil`.

The bundle scans its Mach-O executable and returns all of the architecture types it finds. Because they are taken directly from the executable, the values may not always correspond to one of the well-known CPU types defined in [`Mach-O Architecture`](1495005-mach-o-architecture.md).

## See Also

- [func preflight() throws](bundle/preflight.md)
  Returns a Boolean value indicating whether the bundle’s executable code could be loaded successfully.
- [func load() -> Bool](bundle/load.md)
  Dynamically loads the bundle’s executable code into a running program, if the code has not already been loaded.
- [func loadAndReturnError() throws](bundle/loadandreturnerror.md)
  Loads the bundle’s executable code and returns any errors.
- [func unload() -> Bool](bundle/unload.md)
  Unloads the code associated with the receiver.
- [var isLoaded: Bool](bundle/isloaded.md)
  The load status of a bundle.
- [Mach-O Architecture](1495005-mach-o-architecture.md)
  Constants that describe the CPU types that a bundle’s executable code supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/executablearchitectures)*