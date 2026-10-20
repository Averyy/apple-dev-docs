# addAccessoryView(to:)

**Framework**: Quartz  
**Kind**: method  
**Role**: Instance Method

Adds `IKSaveOptions` accessory view to a `NSSavePanel`.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func addAccessoryView(to savePanel: NSSavePanel!)
```

```objc
- (void) addSaveOptionsAccessoryViewToSavePanel:(NSSavePanel *) savePanel;
```

## Parameters

- `savePanel`: The save panel to add the `IKSaveOptions` to.

## See Also

### Creating A Save Options Accessory View
- [init!(imageProperties: [AnyHashable : Any]!, imageUTType: String!)](./init%28imageproperties,imageuttype%29.md)
  Initializes a save options accessory pane for the provided image properties and uniform type identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/iksaveoptions/addaccessoryview(to:))*