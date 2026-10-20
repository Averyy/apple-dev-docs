# deviceDescription

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A dictionary of keys and values that describe the device.

**Availability**:
- macOS

## Declaration

```swift
var deviceDescription: [NSDeviceDescriptionKey : Any] { get }
```

```objc
@property (copy, readonly) NSDictionary<NSString *,id> * deviceDescription;
```

#### Return Value

A dictionary of the device properties. See `NSGraphics.h` for possible keys. The only key guaranteed to exist is `NSDeviceIsPrinter`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprinter/devicedescription)*