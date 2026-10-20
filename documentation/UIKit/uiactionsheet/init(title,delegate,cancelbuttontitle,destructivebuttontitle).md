# init(title:delegate:cancelButtonTitle:destructiveButtonTitle:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Initializes the action sheet using the specified starting parameters.

**Availability**:
- iOS 2.0+ - Deprecated in 8.3
- iPadOS 2.0+ - Deprecated in 8.3
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: For more information, see [`UIActionSheet`](../uiactionsheet.md).

## Declaration

```swift
init(title: String?, delegate: (any UIActionSheetDelegate)?, cancelButtonTitle: String?, destructiveButtonTitle: String?)
```

```objc
- (instancetype) initWithTitle:(NSString *) title delegate:(id<UIActionSheetDelegate>) delegate cancelButtonTitle:(NSString *) cancelButtonTitle destructiveButtonTitle:(NSString *) destructiveButtonTitle otherButtonTitles:(NSString *) otherButtonTitles;
```

#### Return Value

A newly initialized action sheet.

#### Discussion

The action sheet automatically sets the appearance of the destructive and cancel buttons. If the action sheet contains only one button, it doesn’t apply the custom colors associated with the destructive and cancel buttons.

## Parameters

- `title`: A string to display in the title area of the action sheet. Pass `nil` if you don’t want to display any text in the title area.
- `delegate`: The receiver’s delegate object. Although this parameter may be `nil`, the delegate is used to respond to taps in the action sheet and should usually be provided.
- `cancelButtonTitle`: The title of the cancel button. This button is added to the action sheet automatically and assigned an appropriate index, which is available from the [`cancelButtonIndex`](./cancelbuttonindex.md) property. This button is displayed in black to indicate that it represents the cancel action. Specify `nil` if you don’t want a cancel button or are presenting the action sheet on an iPad.
- `destructiveButtonTitle`: The title of the destructive button. This button is added to the action sheet automatically and assigned an appropriate index, which is available from the [`destructiveButtonIndex`](./destructivebuttonindex.md) property. This button is displayed in red to indicate that it represents a destructive behavior. Specify `nil` if you don’t want a destructive button.

## See Also

### Creating action sheets
- [convenience init(title: String?, delegate: (any UIActionSheetDelegate)?, cancelButtonTitle: String?, destructiveButtonTitle: String?, otherButtonTitles: String, String...)](./init%28title,delegate,cancelbuttontitle,destructivebuttontitle,otherbuttontitles,_%29.md)
  Creates an action sheet with the specified values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactionsheet/init(title:delegate:cancelbuttontitle:destructivebuttontitle:))*