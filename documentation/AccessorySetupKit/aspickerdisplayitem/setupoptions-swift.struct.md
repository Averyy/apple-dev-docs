# ASPickerDisplayItem.SetupOptions

**Framework**: AccessorySetupKit  
**Kind**: struct  
**Role**: Structure

Setup options offered by the accessory picker.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct SetupOptions
```

```c
enum ASPickerDisplayItemSetupOptions : NSUInteger;
```

## Topics

### Creating an options instance
- [init(rawValue: UInt)](./setupoptions-swift.struct/init%28rawvalue%29.md)
### Options
- [static var rename: ASPickerDisplayItem.SetupOptions](./setupoptions-swift.struct/rename.md)
  An option to ask the person using the app to rename the accessory.
- [static var confirmAuthorization: ASPickerDisplayItem.SetupOptions](./setupoptions-swift.struct/confirmauthorization.md)
  An option to require the app to finish accessory authorization before showing the setup view.
- [static var finishInApp: ASPickerDisplayItem.SetupOptions](./setupoptions-swift.struct/finishinapp.md)
  An option to ask the person setting up the accessory to finish additional setup in the app after the accessory is authorized.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Customizing setup options
- [var setupOptions: ASPickerDisplayItem.SetupOptions](./setupoptions-swift.property.md)
  Custom setup options for the accessory.
- [var renameOptions: ASAccessory.RenameOptions](./renameoptions.md)
  Options to allow renaming a matched accessory.
- [ASAccessory.RenameOptions](../asaccessory/renameoptions.md)
  Options that affect the behavior of an accessory renaming operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aspickerdisplayitem/setupoptions-swift.struct)*