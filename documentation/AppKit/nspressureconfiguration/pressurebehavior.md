# pressureBehavior

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The pressure behavior of the pressure configuration object.

**Availability**:
- macOS 10.10.3+

## Declaration

```swift
var pressureBehavior: NSEvent.PressureBehavior { get }
```

```objc
@property (readonly) NSPressureBehavior pressureBehavior;
```

## Discussion

The value of this property is set when the pressure configuration object is created and cannot be changed later. It contains the pressure behavior type of the pressure configuration object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspressureconfiguration/pressurebehavior)*