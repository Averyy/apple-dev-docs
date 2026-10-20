# isFindNavigatorVisible

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates when the find panel displays onscreen.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
var isFindNavigatorVisible: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isFindNavigatorVisible) BOOL findNavigatorVisible;
```

#### Discussion

The value of this property is `YES` when the find panel displays; otherwise, `NO`.

## See Also

### Configuring the find panel
- [var searchText: String?](./searchtext.md)
  The search query with which to prepopulate the find panel’s search text field.
- [var replacementText: String?](./replacementtext.md)
  The replacement string with which to prepopulate the find panel’s replace text field.
- [var optionsMenuProvider: (([UIMenuElement]) -> UIMenu?)?](./optionsmenuprovider.md)
  A closure that populates the search options for a find interaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifindinteraction/isfindnavigatorvisible)*