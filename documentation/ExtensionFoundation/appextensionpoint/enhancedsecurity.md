# AppExtensionPoint.EnhancedSecurity

**Framework**: ExtensionFoundation  
**Kind**: struct

Specifies that the extension bound to this extension point must be launched in enhanced security mode

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
struct EnhancedSecurity
```

#### Overview

When enabled extensions will only have access to `XPCSession` based IPC and will run in a restrictive sandbox. Enhanced security extensions cannot provide remote user interface.

## Topics

### Initializers
- [init(Bool)](appextensionpoint/enhancedsecurity/init(_:).md)

## Relationships

### Conforms To
- [AppExtensionPoint.Attribute](appextensionpoint/attribute.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/enhancedsecurity)*