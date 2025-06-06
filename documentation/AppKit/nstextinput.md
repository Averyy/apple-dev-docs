# NSTextInput

**Framework**: AppKit  
**Kind**: protocol

A set of methods that text views need to implement to interact properly with the text input management system.

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSTextInput
```

#### Overview

> ❗ **Important**:  [`NSTextInput`](nstextinput.md) protocol is slated for deprecation. Please use the [`NSTextInputClient`](nstextinputclient.md) protocol instead.

 [`NSTextInput`](nstextinput.md) protocol is slated for deprecation. Please use the [`NSTextInputClient`](nstextinputclient.md) protocol instead.

`NSTextView` and its abstract superclass `NSText` are the only classes included in Cocoa that implement `NSTextInput`. To create another text view class, you can either subclass `NSTextView` (and not `NSText`, for historical reasons), or subclass `NSView` and implement the `NSTextInput` protocol.

> ❗ **Important**:  Methods specific to the `NSTextInput` protocol are intended for dealing with text input and generally are not suitable for other purposes.

 Methods specific to the `NSTextInput` protocol are intended for dealing with text input and generally are not suitable for other purposes.

## Relationships

### Conforming Types
- [NSTextView](nstextview.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextinput)*