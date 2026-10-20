# insertElements(_:atStartOfMenu:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Insert elements at the start of an identified parent menu.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func insertElements(_ childElements: [UIMenuElement], atStartOfMenu parentIdentifier: UIMenu.Identifier)
```

```objc
- (void) insertElements:(NSArray<UIMenuElement *> *) childElements atStartOfMenuForIdentifier:(UIMenuIdentifier) parentIdentifier;
```

## Parameters

- `childElements`: The child elements to insert.
- `parentIdentifier`: The identifier of the parent menu to insert elements at the start of.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/insertelements(_:atstartofmenu:))*