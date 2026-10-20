# load()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) load;
```

#### Return Value

[`true`](../../Swift/true.md) if the method successfully loads the bundle’s code or if the code has already been loaded, otherwise [`false`](../../Swift/false.md).

#### Discussion

You can use this method to load the code associated with a dynamically loaded bundle, such as a plug-in or framework. Prior to OS X version 10.5, a bundle would attempt to load its code—if it had any—only once. Once loaded, you could not unload that code. In macOS 10.5 and later, you can unload a bundle’s executable code using the [`unload()`](./unload%28%29.md) method.

You don’t need to load a bundle’s executable code to search the bundle’s resources.

This method initializes the principal class in the bundle. To add code you want executed after loading, override the [`initialize()`](../../ObjectiveC/nsobject-swift.class/initialize%28%29.md) class method of the principal class.

##### Special Considerations

If an `NSBundle` object calls the [`load()`](./load%28%29.md) method, it calls the [`unload()`](./unload%28%29.md) method before being deallocated. Therefore, you should retain any `NSBundle` object for as long as any code from it is used by the app.

## See Also

### Related Documentation
- [var principalClass: AnyClass?](./principalclass.md)
  The bundle’s principal class.
- [func classNamed(String) -> AnyClass?](./classnamed%28_%29.md)
  Returns the `Class` object for the specified name.
### Loading code from a bundle
- [var executableArchitectures: [NSNumber]?](./executablearchitectures.md)
  An array of numbers indicating the architecture types supported by the bundle’s executable.
- [func preflight() throws](./preflight%28%29.md)
  Returns a Boolean value indicating whether the bundle’s executable code could be loaded successfully.
- [func loadAndReturnError() throws](./loadandreturnerror%28%29.md)
  Loads the bundle’s executable code and returns any errors.
- [func unload() -> Bool](./unload%28%29.md)
  Unloads the code associated with the receiver.
- [var isLoaded: Bool](./isloaded.md)
  The load status of a bundle.
- [Mach-O Architecture](../api-1495005-mach-o-architecture.md)
  Constants that describe the CPU types that a bundle’s executable code supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/load())*