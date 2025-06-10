# onInterruption

**Framework**: ExtensionFoundation  
**Kind**: property

A closure the system calles when an extension process exits.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 13.0+
- tvOS 26.0+ (Beta)
- visionOS 1.1+
- watchOS 26.0+ (Beta)

## Declaration

```swift
var onInterruption: () -> Void
```

#### Discussion

A closure that the system calls if the extension process created from this configuration exits. The configuration sets this property to nil before it calls the handler block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess/configuration/oninterruption)*