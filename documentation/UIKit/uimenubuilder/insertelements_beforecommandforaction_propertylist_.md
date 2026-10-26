# insertElements:beforeCommandForAction:propertyList:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Insert elements before an identified command.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) insertElements:(NSArray<UIMenuElement *> *) insertedElements beforeCommandForAction:(SEL) siblingAction propertyList:(id) siblingPropertyList;
```

## Parameters

- `insertedElements`: The elements to insert.
- `siblingAction`: The action of the command to insert elements before.
- `siblingPropertyList`: Property list object to distinguish commands, if needed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/insertelements:beforecommandforaction:propertylist:)*