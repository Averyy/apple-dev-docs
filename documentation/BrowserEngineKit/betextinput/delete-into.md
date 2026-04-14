# delete(in:to:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Deletes the specified amount of text.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func delete(in direction: UITextStorageDirection, to granularity: UITextGranularity)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

The editing behavior-to-key combinations include:

- **Character backward**: Delete
- **Character forward**: Delete forward (Function + Delete)
- **Word backward**: Option + Delete
- **Word forward**: Option + Delete forward (Function + Delete)
- **Line end**: Command + Delete
- **Line start**: Command + Delete forward (Function + Delete)
- **Paragraph end**: Control + K
- **Paragraph start**: Control + Function + K

## Parameters

- `direction`: The direction in which to delete text, relative to the base writing direction.
- `granularity`: The amount of text to delete.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/delete(in:to:))*