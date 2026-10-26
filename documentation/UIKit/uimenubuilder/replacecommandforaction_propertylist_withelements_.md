# replaceCommandForAction:propertyList:withElements:

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Replace an identified command with menu elements.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```objc
- (void) replaceCommandForAction:(SEL) replacedAction propertyList:(id) replacedPropertyList withElements:(NSArray<UIMenuElement *> *) replacementElements;
```

## Parameters

- `replacedAction`: The action of the command to be replaced.
- `replacedPropertyList`: Property list object to distinguish commands, if needed.
- `replacementElements`: The replacement elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimenubuilder/replacecommandforaction:propertylist:withelements:)*