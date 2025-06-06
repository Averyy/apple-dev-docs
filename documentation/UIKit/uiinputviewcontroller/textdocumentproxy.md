# textDocumentProxy

**Framework**: UIKit  
**Kind**: property

A proxy to the text input object that the custom keyboard is interacting with.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var textDocumentProxy: any UITextDocumentProxy { get }
```

## Mentions

- [Configuring a custom keyboard interface](configuring-a-custom-keyboard-interface.md)

#### Discussion

This property conforms directly or indirectly to the following protocols:

- The [`UITextDocumentProxy`](uitextdocumentproxy.md) protocol provides textual context around the insertion point
- The [`UIKeyInput`](uikeyinput.md) protocol provides the insert and delete methods, and lets you find out if the text object is empty
- The [`UITextInputTraits`](uitextinputtraits.md) protocol provides insight into the characteristics of the text input object, such as whether it requests a style of autocapitalization and which sort of keyboard it expects (for example, email address, URL, number pad, or default).

Employ this property to interact with the current text input object. For example, to insert text you would write code like this:

```objc
[self.textDocumentProxy insertText:@"hello "]; // Inserts the string "hello " at the insertion point
```

To delete text, you’d write code like this:

```objc
[self.textDocumentProxy deleteBackward];       // Deletes the character to the left of the insertion point
```

## See Also

- [protocol UITextDocumentProxy](uitextdocumentproxy.md)
  An object that provides textual context to a custom keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputviewcontroller/textdocumentproxy)*