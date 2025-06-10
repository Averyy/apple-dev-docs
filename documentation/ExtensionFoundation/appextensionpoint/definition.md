# AppExtensionPoint.Definition

**Framework**: ExtensionFoundation  
**Kind**: struct

Marks the property as an extension point definition

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.1+
- watchOS 26.0+ (Beta)

## Declaration

```swift
@resultBuilder
struct Definition
```

#### Overview

When included in an App target, properties of an `ExtensionPointDefining` type wrapped with the `Definition` builder will be compiled into an extension point definition

## Topics

### Type Methods
- [static func buildBlock<each T>(AppExtensionPoint.Name, repeat each T) -> AppExtensionPoint](appextensionpoint/definition/buildblock(_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/definition)*