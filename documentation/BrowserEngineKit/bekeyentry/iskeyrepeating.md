# isKeyRepeating

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the person holds a key down to repeat its key event.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var isKeyRepeating: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isKeyRepeating) BOOL keyRepeating;
```

## Mentions

- [Integrating custom browser text views with UIKit](../integrating-custom-browser-text-views-with-uikit.md)

## See Also

### Getting information about the keypress
- [var state: BEKeyEntry.KeyPressState](./state.md)
  A value that indicates if the key is pressed.
- [BEKeyEntry.KeyPressState](./keypressstate.md)
  Key-press states for a keyboard event.
- [var timestamp: TimeInterval](./timestamp.md)
  The time that the key event occurs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeyentry/iskeyrepeating)*