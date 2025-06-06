# init(componentDescription:)

**Framework**: Audiotoolbox  
**Kind**: init

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
convenience init(componentDescription: AudioComponentDescription) throws
```

#### Return Value

An initialized audio unit, or `nil` if initialization failed.

#### Discussion

This is the convenience initializer.

A single audio unit subclass may implement multiple audio units—for example, an effect that can also function as a generator, or a cluster of related effects.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `componentDescription`: The component to instantiate.

## See Also

- [init(componentDescription: AudioComponentDescription, options: AudioComponentInstantiationOptions) throws](auaudiounit/init(componentdescription:options:).md)
  Synchronously initializes a new audio unit object.
- [class func instantiate(with: AudioComponentDescription, options: AudioComponentInstantiationOptions, completionHandler: (AUAudioUnit?, (any Error)?) -> Void)](auaudiounit/instantiate(with:options:completionhandler:).md)
  Asynchronously creates an audio unit instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/init(componentdescription:))*