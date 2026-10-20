# UIDocumentBrowserAction.Availability

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

Values that determine where the action can appear in the document browser.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct Availability
```

```c
enum UIDocumentBrowserActionAvailability : NSInteger;
```

## Topics

### Constants
- [static var menu: UIDocumentBrowserAction.Availability](./availability-swift.struct/menu.md)
  An action that appears in the Edit Menu when the user long presses a supported document.
- [static var navigationBar: UIDocumentBrowserAction.Availability](./availability-swift.struct/navigationbar.md)
  An action that appears in the navigation bar when the user puts the document browser in Select mode.
### Initializers
- [init(rawValue: Int)](./availability-swift.struct/init%28rawvalue%29.md)
  Returns a newly instantiated availability instance.

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

### Accessing activity data
- [var identifier: String](./identifier.md)
  The action’s unique identifier.
- [var localizedTitle: String](./localizedtitle.md)
  The title that appears in the menu or navigation bar.
- [var availability: UIDocumentBrowserAction.Availability](./availability-swift.property.md)
  A value that defines where the action can appear (in the Edit Menu, the navigation bar, or both).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/availability-swift.struct)*