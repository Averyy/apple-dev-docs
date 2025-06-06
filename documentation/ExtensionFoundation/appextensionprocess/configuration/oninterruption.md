# onInterruption

**Framework**: ExtensionFoundation  
**Kind**: property

A closure the system calles when an extension process exits.

**Availability**:
- macOS 13.0+

## Declaration

```swift
var onInterruption: () -> Void
```

#### Discussion

A closure that the system calls if the extension process created from this configuration exits. The configuration sets this property to nil before it calls the handler block.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionprocess/configuration/oninterruption)*