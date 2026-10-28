# renameOptions

**Framework**: AccessorySetupKit  
**Kind**: property  
**Role**: Instance Property

Options to allow renaming a matched accessory.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
var renameOptions: ASAccessory.RenameOptions { get set }
```

```objc
@property (nonatomic, assign, readwrite) ASAccessoryRenameOptions renameOptions;
```

## Discussion

To permit renaming, include [`rename`](./setupoptions-swift.struct/rename.md) in the [`setupOptions`](./setupoptions-swift.property.md)

## See Also

### Customizing setup options
- [var setupOptions: ASPickerDisplayItem.SetupOptions](./setupoptions-swift.property.md)
  Custom setup options for the accessory.
- [ASPickerDisplayItem.SetupOptions](./setupoptions-swift.struct.md)
  Setup options offered by the accessory picker.
- [ASAccessory.RenameOptions](../asaccessory/renameoptions.md)
  Options that affect the behavior of an accessory renaming operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/aspickerdisplayitem/renameoptions)*