# load()

**Framework**: Foundation  
**Kind**: method

Dynamically loads the bundle’s executable code into a running program, if the code has not already been loaded.

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
func load() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the method successfully loads the bundle’s code or if the code has already been loaded, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

You can use this method to load the code associated with a dynamically loaded bundle, such as a plug-in or framework. Prior to OS X version 10.5, a bundle would attempt to load its code—if it had any—only once. Once loaded, you could not unload that code. In macOS 10.5 and later, you can unload a bundle’s executable code using the [`unload()`](bundle/unload().md) method.

You don’t need to load a bundle’s executable code to search the bundle’s resources.

This method initializes the principal class in the bundle. To add code you want executed after loading, override the [`initialize()`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/initialize()) class method of the principal class.

##### Special Considerations

If an `NSBundle` object calls the [`load()`](bundle/load().md) method, it calls the [`unload()`](bundle/unload().md) method before being deallocated. Therefore, you should retain any `NSBundle` object for as long as any code from it is used by the app.

## See Also

- [var principalClass: AnyClass?](bundle/principalclass.md)
  The bundle’s principal class.
- [func classNamed(String) -> AnyClass?](bundle/classnamed(_:).md)
  Returns the `Class` object for the specified name.
- [var executableArchitectures: [NSNumber]?](bundle/executablearchitectures.md)
  An array of numbers indicating the architecture types supported by the bundle’s executable.
- [func preflight() throws](bundle/preflight.md)
  Returns a Boolean value indicating whether the bundle’s executable code could be loaded successfully.
- [func loadAndReturnError() throws](bundle/loadandreturnerror.md)
  Loads the bundle’s executable code and returns any errors.
- [func unload() -> Bool](bundle/unload.md)
  Unloads the code associated with the receiver.
- [var isLoaded: Bool](bundle/isloaded.md)
  The load status of a bundle.
- [Mach-O Architecture](1495005-mach-o-architecture.md)
  Constants that describe the CPU types that a bundle’s executable code supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/load())*