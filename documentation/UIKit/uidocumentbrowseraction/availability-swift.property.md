# availability

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A value that defines where the action can appear (in the Edit Menu, the navigation bar, or both).

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var availability: UIDocumentBrowserAction.Availability { get }
```

```objc
@property (nonatomic, readonly) UIDocumentBrowserActionAvailability availability;
```

## Discussion

For a list of possible values, see [`UIDocumentBrowserAction.Availability`](./availability-swift.struct.md).

## See Also

### Accessing activity data
- [var identifier: String](./identifier.md)
  The action’s unique identifier.
- [var localizedTitle: String](./localizedtitle.md)
  The title that appears in the menu or navigation bar.
- [UIDocumentBrowserAction.Availability](./availability-swift.struct.md)
  Values that determine where the action can appear in the document browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowseraction/availability-swift.property)*