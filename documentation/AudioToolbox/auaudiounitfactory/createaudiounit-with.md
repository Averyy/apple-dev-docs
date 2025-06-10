# createAudioUnit(with:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Required**: Yes

Creates an instance of an extension’s audio unit.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func createAudioUnit(with desc: AudioComponentDescription) throws -> AUAudioUnit
```

#### Return Value

An instance of the extension’s audio unit.

#### Discussion

This method is called only once per factory instance.

> **Note**:  In non-ARC code, “create” methods return unretained objects (unlike C “create” functions). In this scenario, you should return an object with a reference count of 1, but autoreleased.

> **Note**:  In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure. You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [`Error Handling`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [`The Swift Programming Language`](https://developer.apple.comhttps://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## Parameters

- `desc`: The description of the audio component.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounitfactory/createaudiounit(with:))*