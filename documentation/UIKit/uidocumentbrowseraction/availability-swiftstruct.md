# UIDocumentBrowserAction.Availability

**Framework**: UIKit  
**Kind**: struct

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

## Topics

### Constants
- [static var menu: UIDocumentBrowserAction.Availability](uidocumentbrowseraction/availability-swift.struct/menu.md)
  An action that appears in the Edit Menu when the user long presses a supported document.
- [static var navigationBar: UIDocumentBrowserAction.Availability](uidocumentbrowseraction/availability-swift.struct/navigationbar.md)
  An action that appears in the navigation bar when the user puts the document browser in Select mode.
### Initializers
- [init(rawValue: Int)](uidocumentbrowseraction/availability-swift.struct/init(rawvalue:).md)
  Returns a newly instantiated availability instance.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [var identifier: String](uidocumentbrowseraction/identifier.md)
  The action’s unique identifier.
- [var localizedTitle: String](uidocumentbrowseraction/localizedtitle.md)
  The title that appears in the menu or navigation bar.
- [var availability: UIDocumentBrowserAction.Availability](uidocumentbrowseraction/availability-swift.property.md)
  A value that defines where the action can appear (in the Edit Menu, the navigation bar, or both).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/availability-swift.struct)*