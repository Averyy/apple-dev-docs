# replace(menu:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Replace an identified menu with menu elements.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func replace(menu replacedIdentifier: UIMenu.Identifier, with replacementElements: [UIMenuElement])
```

```objc
- (void) replaceMenuForIdentifier:(UIMenuIdentifier) replacedIdentifier withElements:(NSArray<UIMenuElement *> *) replacementElements;
```

## Parameters

- `replacedIdentifier`: The identifier of the menu to be replaced.
- `replacementElements`: The replacement elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/replace(menu:with:)-8mwou)*