# Mach-O Architecture

**Framework**: Foundation

Constants that describe the CPU types that a bundle’s executable code supports.

## Topics

### Constants
- [var NSBundleExecutableArchitectureARM64: Int](nsbundleexecutablearchitecturearm64.md)
  The 64-bit ARM architecture.
- [var NSBundleExecutableArchitectureI386: Int](nsbundleexecutablearchitecturei386.md)
  The 32-bit Intel architecture.
- [var NSBundleExecutableArchitectureX86_64: Int](nsbundleexecutablearchitecturex86_64.md)
  The 64-bit Intel architecture.
- [var NSBundleExecutableArchitecturePPC: Int](nsbundleexecutablearchitectureppc.md)
  The 32-bit PowerPC architecture.
- [var NSBundleExecutableArchitecturePPC64: Int](nsbundleexecutablearchitectureppc64.md)
  The 64-bit PowerPC architecture.

## See Also

- [var executableArchitectures: [NSNumber]?](bundle/executablearchitectures.md)
  An array of numbers indicating the architecture types supported by the bundle’s executable.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/1495005-mach-o-architecture)*