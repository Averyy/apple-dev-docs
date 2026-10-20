# isLoaded

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The load status of a bundle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isLoaded: Bool { get }
```

```objc
@property (readonly, getter=isLoaded) BOOL loaded;
```

#### Discussion

[`true`](../../Swift/true.md) if the bundle’s code is currently loaded, otherwise [`false`](../../Swift/false.md).

## See Also

### Loading code from a bundle
- [var executableArchitectures: [NSNumber]?](./executablearchitectures.md)
  An array of numbers indicating the architecture types supported by the bundle’s executable.
- [func preflight() throws](./preflight%28%29.md)
  Returns a Boolean value indicating whether the bundle’s executable code could be loaded successfully.
- [func load() -> Bool](./load%28%29.md)
  Dynamically loads the bundle’s executable code into a running program, if the code has not already been loaded.
- [func loadAndReturnError() throws](./loadandreturnerror%28%29.md)
  Loads the bundle’s executable code and returns any errors.
- [func unload() -> Bool](./unload%28%29.md)
  Unloads the code associated with the receiver.
- [Mach-O Architecture](../api-1495005-mach-o-architecture.md)
  Constants that describe the CPU types that a bundle’s executable code supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/isloaded)*