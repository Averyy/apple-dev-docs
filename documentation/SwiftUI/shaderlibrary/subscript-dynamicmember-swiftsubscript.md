# subscript(dynamicMember:)

**Framework**: SwiftUI  
**Kind**: subscript

Returns a new shader function representing the stitchable MSL function in the library called `name`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
subscript(dynamicMember name: String) -> ShaderFunction { get }
```

#### Overview

Typically this subscript is used implicitly via the dynamic member syntax, for example:

let fn = ShaderLibrary.default.myFunction

which creates a reference to the MSL function called `myFunction()`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/shaderlibrary/subscript(dynamicmember:)-swift.subscript)*