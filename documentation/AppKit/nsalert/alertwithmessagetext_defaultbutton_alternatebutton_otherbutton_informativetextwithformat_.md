# alertWithMessageText:defaultButton:alternateButton:otherButton:informativeTextWithFormat:

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Creates an alert compatible with alerts created using the [`NSRunAlertPanel`](../nsrunalertpanel.md) function for display as a warning-style alert.

**Availability**:
- macOS 10.3+ - Deprecated in 10.10

> **Deprecated**: Instead, `alloc` and `init` an `NSAlert` object and set its attributes as appropriate.

## Declaration

```objc
+ (NSAlert *) alertWithMessageText:(NSString *) message defaultButton:(NSString *) defaultButton alternateButton:(NSString *) alternateButton otherButton:(NSString *) otherButton informativeTextWithFormat:(NSString *) format;
```

#### Return Value

Initialized alert.

#### Discussion

For languages that read left to right, the buttons are laid out on the bottom-right corner of the alert sheet or window, with `defaultButtonTitle` on the right, `alternateButtonTitle` on the left, and `otherButtonTitle` in the middle.  The return values identifying these buttons are constants— `NSAlertDefaultReturn`, `NSAlertAlternateReturn`, and `NSAlertOtherReturn`—that correspond to the keywords.

By default, the first button has a key equivalent of Return, any button with a title of “Cancel” has a key equivalent of Escape, and any button with the title “Don’t Save” has a key equivalent of Command-D (but only if it is not the first button). You can also assign different key equivalents for the buttons using the [`keyEquivalent`](../nsbutton/keyequivalent.md) method of the `NSButton` class. To access the alert’s buttons, use the [`buttons`](./buttons.md) property.

##### Special Considerations

This is a compatibility method. It is designed for easy adoption by apps migrating from the corresponding function-based API. This method uses earlier return values—`NSAlertDefaultReturn`, `NSAlertAlternateReturn`, and `NSAlertOtherReturn`—compatible with the earlier API, rather than the return values defined by the `NSAlert` class, described in `Button Return Values`.

Unless you must maintain compatibility with existing alert-processing code that uses the function-based API, you should allocate (`alloc`) and initialize (`init`) the object, and then set its attributes using the appropriate methods of the `NSAlert` class.

## Parameters

- `message`: Title of the alert. When `nil` or an empty string, a default localized title is used (“Alert” in English).
- `defaultButton`: Title for the default button. When `nil` or an empty string, a default localized button title (“OK” in English) is used.
- `alternateButton`: Title for the alternate button. When `nil`, the alternate button is not created.
- `otherButton`: Title for the other button. When `nil`, the other button is not created.
- `format`: Informative text. This is optional but must be an empty string (`@””`) not `nil`. Can embed variable values using a format string; list any necessary arguments for this formatted string at the end of the method’s argument list. For more information on format strings, see [Formatting String Objects](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Strings/Articles/FormatStrings.html#//apple_ref/doc/uid/20000943).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/alertwithmessagetext:defaultbutton:alternatebutton:otherbutton:informativetextwithformat:)*