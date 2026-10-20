# optionsMenuProvider

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A closure that populates the search options for a find interaction.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var optionsMenuProvider: (([UIMenuElement]) -> UIMenu?)? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) UIMenu * (^optionsMenuProvider)(NSArray<UIMenuElement *> *defaultOptions);
```

#### Discussion

You use this closure to modify, augement or omit options from the default set available in [`UITextSearchOptions`](../uitextsearchoptions.md).

## See Also

### Configuring the find panel
- [var isFindNavigatorVisible: Bool](./isfindnavigatorvisible.md)
  A Boolean value that indicates when the find panel displays onscreen.
- [var searchText: String?](./searchtext.md)
  The search query with which to prepopulate the find panel’s search text field.
- [var replacementText: String?](./replacementtext.md)
  The replacement string with which to prepopulate the find panel’s replace text field.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteraction/optionsmenuprovider)*