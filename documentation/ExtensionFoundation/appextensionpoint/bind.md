# AppExtensionPoint.Bind

**Framework**: ExtensionFoundation  
**Kind**: struct

Marks the property as a binding to an extension point

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
struct Bind
```

#### Overview

When included in an AppExtension target, the `AppExtension.boundAppExtensionPoint` will binding the appex to the extension point specified by `AppExtensionPoint.Identifier`. This

## Topics

### Type Methods
- [static func buildBlock(AppExtensionPoint.Identifier) -> AppExtensionPoint](appextensionpoint/bind/buildblock(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/bind)*