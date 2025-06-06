# defaultUsername

**Framework**: ImageCaptureCore  
**Kind**: property

A default username on protected scanners.

**Availability**:
- macOS 10.4+

## Declaration

```swift
var defaultUsername: String { get set }
```

#### Discussion

If the scanner is protected, you can set this property to a specific username as a convenience, instead of prompting the user for a username. The value persists until reset to `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icscannerdevice/defaultusername)*