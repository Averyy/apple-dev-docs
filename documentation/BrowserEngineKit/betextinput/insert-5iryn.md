# insert(_:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Inserts a `textSuggestion` in response to a user suggestion selection

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func insert(_ textSuggestion: BETextSuggestion)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

Inserts suggested text.

#### Overview

The system calls this method to suggest insertions into the text view, for example AutoFill credentials.

## Parameters

- `textSuggestion`: The suggestion to insert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/insert(_:)-5iryn)*