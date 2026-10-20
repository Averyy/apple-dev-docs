# init(imageProperties:imageUTType:)

**Framework**: Quartz  
**Kind**: init  
**Role**: Initializer

Initializes a save options accessory pane for the provided image properties and uniform type identifier.

**Availability**:
- macOS 10.5+

## Declaration

```swift
init!(imageProperties: [AnyHashable : Any]!, imageUTType: String!)
```

```objc
- (instancetype) initWithImageProperties:(NSDictionary *) imageProperties imageUTType:(NSString *) imageUTType;
```

#### Return Value

The initialized object.

## Parameters

- `imageProperties`: A dictionary of image properties.
- `imageUTType`: A string that specifies a uniform type identifier, such as  `JPEG`. See [Uniform Type Identifiers Overview](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/understanding_utis/understand_utis_intro/understand_utis_intro.html#//apple_ref/doc/uid/TP40001319).

## See Also

### Creating A Save Options Accessory View
- [func addAccessoryView(to: NSSavePanel!)](./addaccessoryview%28to%29.md)
  Adds `IKSaveOptions` accessory view to a `NSSavePanel`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/iksaveoptions/init(imageproperties:imageuttype:))*