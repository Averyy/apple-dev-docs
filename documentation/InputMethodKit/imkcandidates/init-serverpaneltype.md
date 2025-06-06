# init(server:panelType:)

**Framework**: InputMethodKit  
**Kind**: init

Returns the initialized `IMKCandidates` object.

**Availability**:
- macOS 10.5+

## Declaration

```swift
@MainActor
init!(server: IMKServer!, panelType: IMKCandidatePanelType)
```

#### Return Value

The initialized `IMKCandidates` object.

#### Discussion

When an input method allocates an `IMKCandidates` object it should initialize that object by calling this method.

## Parameters

- `server`: The   object that manages the candidate and the panel type.
- `panelType`: A panel type for the candidate window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/inputmethodkit/imkcandidates/init(server:paneltype:))*