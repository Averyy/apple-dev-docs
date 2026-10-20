# replace(action:with:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Replace an identified action with menu elements.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func replace(action replacedIdentifier: UIAction.Identifier, with replacementElements: [UIMenuElement])
```

```objc
- (void) replaceActionForIdentifier:(UIActionIdentifier) replacedIdentifier withElements:(NSArray<UIMenuElement *> *) replacementElements;
```

## Parameters

- `replacedIdentifier`: The identifier of the action to be replaced.
- `replacementElements`: The replacement elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/replace(action:with:))*