# ASPickerDisplayItem.SetupOptions

**Framework**: AccessorySetupKit  
**Kind**: struct

Setup options offered by the accessory picker.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct SetupOptions
```

## Topics

### Creating an options instance
- [init(rawValue: UInt)](aspickerdisplayitem/setupoptions-swift.struct/init(rawvalue:).md)
### Options
- [static var rename: ASPickerDisplayItem.SetupOptions](aspickerdisplayitem/setupoptions-swift.struct/rename.md)
  An option to ask the person using the app to rename the accessory.
- [static var confirmAuthorization: ASPickerDisplayItem.SetupOptions](aspickerdisplayitem/setupoptions-swift.struct/confirmauthorization.md)
  An option to require the app to finish accessory authorization before showing the setup view.
- [static var finishInApp: ASPickerDisplayItem.SetupOptions](aspickerdisplayitem/setupoptions-swift.struct/finishinapp.md)
  An option to ask the person setting up the accessory to finish additional setup in the app after the accessory is authorized.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [var setupOptions: ASPickerDisplayItem.SetupOptions](aspickerdisplayitem/setupoptions-swift.property.md)
  Custom setup options for the accessory.
- [var renameOptions: ASAccessory.RenameOptions](aspickerdisplayitem/renameoptions.md)
  Options to allow renaming a matched accessory.
- [ASAccessory.RenameOptions](asaccessory/renameoptions.md)
  Options that affect the behavior of an accessory renaming operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aspickerdisplayitem/setupoptions-swift.struct)*