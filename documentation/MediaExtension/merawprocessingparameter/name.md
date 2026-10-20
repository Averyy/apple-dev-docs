# name

**Framework**: MediaExtension  
**Kind**: property  
**Role**: Instance Property

A localized human-readable name for the parameter, suitable for displaying in application UI.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var name: String { get }
```

```objc
@property (readonly) NSString * name;
```

## See Also

### Inspecting a processing parameter
- [var enabled: Bool](./enabled.md)
  A Boolean value that indicates whether the extension enables the parameter.
- [var key: String](./key.md)
  A unique key string identifying the parameter.
- [var longDescription: String](./longdescription.md)
  A localized description of the parameter, suitable for displaying in a tool tip or similar explanatory UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/merawprocessingparameter/name)*