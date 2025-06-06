# provideNewView(_:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the view containing the receiver’s user interface.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func provideNewView(_ initialRequest: Bool) -> NSView
```

#### Return Value

The view containing the color picker’s user interface. The `NSView` returned by this method should be set to automatically resize both its width and height.

#### Discussion

This message is sent to the color picker whenever the color panel attempts to display it. This may be when the panel is first presented, when the user switches pickers, or when the picker is switched through an API.

## Parameters

- `initialRequest`:   only when this method is first invoked for your color picker. If   is  , the method should perform any initialization required (such as lazily loading a nib file, initializing the view, or performing any other custom initialization required for your picker).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolorpickingcustom/providenewview(_:))*