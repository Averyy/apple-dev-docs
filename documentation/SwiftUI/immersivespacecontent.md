# ImmersiveSpaceContent

**Framework**: SwiftUI  
**Kind**: protocol

A type that you can use as the content of an immersive space.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency protocol ImmersiveSpaceContent
```

#### Overview

A type conforming to this protocol inherits `@preconcurrency @MainActor` isolation from the protocol if the conformance is included in the type’s base declaration:

```swift
struct MyCustomType: Transition {
    // `@preconcurrency @MainActor` isolation by default
}
```

Isolation to the main actor is the default, but it’s not required. Declare the conformance in an extension to opt out of main actor isolation:

```swift
extension MyCustomType: Transition {
    // `nonisolated` by default
}
```

## Topics

### Creating immersive space content
- [var body: Self.Body](immersivespacecontent/body-swift.property.md)
- [associatedtype Body : ImmersiveSpaceContent](immersivespacecontent/body-swift.associatedtype.md)

## Relationships

### Conforming Types
- [CompositorContentBuilder.Content](compositorcontentbuilder/content.md)
- [ImmersiveSpaceViewContent](immersivespaceviewcontent.md)

## See Also

- [struct ImmersiveSpaceViewContent](immersivespaceviewcontent.md)
  Immersive space content that uses a SwiftUI view hierarchy as the content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/immersivespacecontent)*