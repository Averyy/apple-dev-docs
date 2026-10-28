# preflight()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the bundle’s executable code could be loaded successfully.

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
func preflight() throws
```

```objc
- (BOOL) preflightAndReturnError:(NSError **) error;
```

## Discussion

This method does not actually load the bundle’s executable code. Instead, it performs several checks to see if the code could be loaded and with one exception returns the same errors that would occur during an actual load operation. The one exception is the `NSExecutableLinkError` error, which requires the actual loading of the code to verify link errors.

For a list of possible load errors, see the discussion for the [`loadAndReturnError()`](./loadandreturnerror%28%29.md) method.

> **Handling Errors in Swift**:  In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Loading code from a bundle
- [var executableArchitectures: [NSNumber]?](./executablearchitectures.md)
  An array of numbers indicating the architecture types supported by the bundle’s executable.
- [func load() -> Bool](./load%28%29.md)
  Dynamically loads the bundle’s executable code into a running program, if the code has not already been loaded.
- [func loadAndReturnError() throws](./loadandreturnerror%28%29.md)
  Loads the bundle’s executable code and returns any errors.
- [func unload() -> Bool](./unload%28%29.md)
  Unloads the code associated with the receiver.
- [var isLoaded: Bool](./isloaded.md)
  The load status of a bundle.
- [Mach-O Architecture](../api-1495005-mach-o-architecture.md)
  Constants that describe the CPU types that a bundle’s executable code supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/bundle/preflight())*