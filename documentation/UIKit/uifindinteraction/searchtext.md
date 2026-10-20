# searchText

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The search query with which to prepopulate the find panel’s search text field.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var searchText: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * searchText;
```

## See Also

### Configuring the find panel
- [var isFindNavigatorVisible: Bool](./isfindnavigatorvisible.md)
  A Boolean value that indicates when the find panel displays onscreen.
- [var replacementText: String?](./replacementtext.md)
  The replacement string with which to prepopulate the find panel’s replace text field.
- [var optionsMenuProvider: (([UIMenuElement]) -> UIMenu?)?](./optionsmenuprovider.md)
  A closure that populates the search options for a find interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteraction/searchtext)*