# deviceDescription

**Framework**: AppKit  
**Kind**: property

A dictionary of keys and values that describe the device.

**Availability**:
- macOS ?+

## Declaration

```swift
var deviceDescription: [NSDeviceDescriptionKey : Any] { get }
```

#### Return Value

A dictionary of the device properties. See `NSGraphics.h` for possible keys. The only key guaranteed to exist is `NSDeviceIsPrinter`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/devicedescription)*