# noteSelectedAlternativeString(_:)

**Framework**: AppKit  
**Kind**: method

Sent to the `NSTextAlternatives` object by the text view when the user chooses one of the alternative strings.

**Availability**:
- macOS 10.8+

## Declaration

```swift
func noteSelectedAlternativeString(_ alternativeString: String)
```

#### Discussion

The base class implementation sends a notification, `NSTextAlternativesSelectedAlternativeStringNotification`, with the selected alternative string in the user info under the key `@"NSAlternativeString"`. Using this mechanism, arbitrary objects can listen for user selections of alternative strings.

## Parameters

- `alternativeString`: The alternative string chosen by the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextalternatives/noteselectedalternativestring(_:))*