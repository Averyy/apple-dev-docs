# init(error:)

**Framework**: AppKit  
**Kind**: init

Returns an alert initialized from information in an error object.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
init(error: any Error)
```

#### Return Value

An initialized alert.

#### Discussion

The `NSAlert` class extracts the localized error description, recovery suggestion, and recovery options from the `error` parameter and uses them as the alert’s message text, informative text, and button titles, respectively.

## Parameters

- `error`: Error information to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsalert/init(error:))*