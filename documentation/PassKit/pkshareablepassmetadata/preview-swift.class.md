# PKShareablePassMetadata.Preview

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS
- visionOS 1.0+

## Declaration

```swift
class Preview
```

```objc
@interface PKShareablePassMetadataPreview : PKAddPassMetadataPreview
```

## Topics

### Initializers
- [init(templateIdentifier: String)](./preview-swift.class/init%28templateidentifier%29.md)
### Instance Properties
- [var ownerDisplayName: String?](./preview-swift.class/ownerdisplayname.md)
- [var provisioningTemplateIdentifier: String?](./preview-swift.class/provisioningtemplateidentifier.md)
### Type Methods
- [+ previewWithTemplateIdentifier:](../pkshareablepassmetadatapreview/previewwithtemplateidentifier_.md)

## Relationships

### Inherits From
- [PKAddPassMetadataPreview](../pkaddpassmetadatapreview.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### General purpose passes
- [class PKSecureElementPass](../pksecureelementpass.md)
  A pass with a credential that the device stores in a certified payment information chip.
- [class PKAddSecureElementPassConfiguration](../pkaddsecureelementpassconfiguration.md)
  An object that describes the configuration of a secure element payment pass.
- [class PKAddSecureElementPassViewController](../pkaddsecureelementpassviewcontroller.md)
  A view controller that manages the addition of secure element payment passes.
- [class PKPass](../pkpass.md)
  An object that represents a single pass.
- [class PKAddPassesViewController](../pkaddpassesviewcontroller.md)
  Lets your app show a pass and prompt the user to add that pass to the pass library.
- [struct AsyncShareablePassConfiguration](../asyncshareablepassconfiguration.md)
- [class PKShareSecureElementPassViewController](../pksharesecureelementpassviewcontroller.md)
- [protocol PKShareSecureElementPassViewControllerDelegate](../pksharesecureelementpassviewcontrollerdelegate.md)
- [enum PKShareSecureElementPassResult](../pksharesecureelementpassresult.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkshareablepassmetadata/preview-swift.class)*