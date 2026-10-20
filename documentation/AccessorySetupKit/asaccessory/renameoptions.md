# ASAccessory.RenameOptions

**Framework**: AccessorySetupKit  
**Kind**: struct  
**Role**: Structure

Options that affect the behavior of an accessory renaming operation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+

## Declaration

```swift
struct RenameOptions
```

```c
enum ASAccessoryRenameOptions : NSUInteger;
```

## Topics

### Creating an options instance
- [init(rawValue: UInt)](./renameoptions/init%28rawvalue%29.md)
### Options
- [static var ssid: ASAccessory.RenameOptions](./renameoptions/ssid.md)
  An option to change an accessory’s SSID along with its display name.

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

### Managing accessories
- [func renameAccessory(ASAccessory, options: ASAccessory.RenameOptions, completionHandler: ((any Error)?) -> Void)](../asaccessorysession/renameaccessory%28_,options,completionhandler%29.md)
  Displays a view to rename an accessory.
- [func removeAccessory(ASAccessory, completionHandler: ((any Error)?) -> Void)](../asaccessorysession/removeaccessory%28_,completionhandler%29.md)
  Removes an accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorysetupkit/asaccessory/renameoptions)*