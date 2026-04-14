# handleKeyEntry(_:completionHandler:)

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Accepts key-entry events from the text system for the text view to process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
func handleKeyEntry(_ entry: BEKeyEntry) async -> (BEKeyEntry, Bool)
```

## Mentions

- [Integrating custom browser text views with UIKit](integrating-custom-browser-text-views-with-uikit.md)

#### Discussion

Implement this method to receive keyboard events from the system. If you handle the `entry` in code, call the completion handler with `true` as the second parameter. Otherwise, call the completion handler with `false` as the second argument, and call the delegate’s [`shouldDeferEventHandlingToSystem(for:context:)`](betextinputdelegate/shoulddefereventhandlingtosystem(for:context:).md) method. In either case, pass the `entry` you received as the first parameter to the completion handler.

The system delivers events on a serial queue, so call the completion handler after your view processes an event to allow the system to send a subsequent event.

## Parameters

- `entry`: The keyboard event delivered by the system.
- `completionHandler`: A block that you call to indicate whether your text view handled the event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/betextinput/handlekeyentry(_:completionhandler:))*