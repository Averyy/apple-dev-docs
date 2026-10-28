# init(componentDescription:options:)

**Framework**: Audio Toolbox  
**Kind**: init  
**Role**: Initializer

Synchronously initializes a new audio unit object.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(componentDescription: AudioComponentDescription, options: AudioComponentInstantiationOptions = []) throws
```

```objc
- (instancetype) initWithComponentDescription:(AudioComponentDescription) componentDescription options:(AudioComponentInstantiationOptions) options error:(NSError **) outError;
```

## Return Value

An initialized audio unit, or `nil` if initialization failed.

## Discussion

This is the designated initializer.

A single audio unit subclass may implement multiple audio units—for example, an effect that can also function as a generator, or a cluster of related effects.

> **Handling Errors in Swift**:  In Swift, this API is imported as an initializer and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `componentDescription`: The component to instantiate.
- `options`: Options for loading the unit in-process or out-of-process.

## See Also

### Creating an Audio Unit
- [convenience init(componentDescription: AudioComponentDescription) throws](./init%28componentdescription%29.md)
  Synchronously initializes a new audio unit object.
- [class func instantiate(with: AudioComponentDescription, options: AudioComponentInstantiationOptions, completionHandler: (AUAudioUnit?, (any Error)?) -> Void)](./instantiate%28with,options,completionhandler%29.md)
  Asynchronously creates an audio unit instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/init(componentdescription:options:))*