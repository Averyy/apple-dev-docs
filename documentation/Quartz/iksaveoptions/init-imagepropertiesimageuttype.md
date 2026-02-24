# init(imageProperties:imageUTType:)

**Framework**: Quartz  
**Kind**: init

Initializes a save options accessory pane for the provided image properties and uniform type identifier.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init!(imageProperties: [AnyHashable : Any]!, imageUTType: String!)
```

#### Return Value

The initialized object.

## Parameters

- `imageProperties`: A dictionary of image properties.
- `imageUTType`: A string that specifies a uniform type identifier, such as  `JPEG`. See [`Uniform Type Identifiers Overview`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319).

## See Also

- [func addAccessoryView(to: NSSavePanel!)](iksaveoptions/addaccessoryview(to:).md)
  Adds `IKSaveOptions` accessory view to a `NSSavePanel`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/iksaveoptions/init(imageproperties:imageuttype:))*