# PKShareSecureElementPassResult

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
enum PKShareSecureElementPassResult
```

```c
enum PKShareSecureElementPassResult : NSInteger;
```

## Topics

### Enumeration Cases
- [PKShareSecureElementPassResult.canceled](./pksharesecureelementpassresult/canceled.md)
- [PKShareSecureElementPassResult.failed](./pksharesecureelementpassresult/failed.md)
- [PKShareSecureElementPassResult.shared](./pksharesecureelementpassresult/shared.md)
### Initializers
- [init?(rawValue: Int)](./pksharesecureelementpassresult/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### General purpose passes
- [class PKSecureElementPass](./pksecureelementpass.md)
  A pass with a credential that the device stores in a certified payment information chip.
- [class PKAddSecureElementPassConfiguration](./pkaddsecureelementpassconfiguration.md)
  An object that describes the configuration of a secure element payment pass.
- [class PKAddSecureElementPassViewController](./pkaddsecureelementpassviewcontroller.md)
  A view controller that manages the addition of secure element payment passes.
- [class PKPass](./pkpass.md)
  An object that represents a single pass.
- [class PKAddPassesViewController](./pkaddpassesviewcontroller.md)
  Lets your app show a pass and prompt the user to add that pass to the pass library.
- [struct AsyncShareablePassConfiguration](./asyncshareablepassconfiguration.md)
- [class PKShareSecureElementPassViewController](./pksharesecureelementpassviewcontroller.md)
- [protocol PKShareSecureElementPassViewControllerDelegate](./pksharesecureelementpassviewcontrollerdelegate.md)
- [PKShareablePassMetadata.Preview](./pkshareablepassmetadata/preview-swift.class.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksharesecureelementpassresult)*