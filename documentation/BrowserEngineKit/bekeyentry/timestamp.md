# timestamp

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property

The time that the key event occurs.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var timestamp: TimeInterval { get }
```

```objc
@property (nonatomic, readonly) NSTimeInterval timestamp;
```

## See Also

### Getting information about the keypress
- [var state: BEKeyEntry.KeyPressState](./state.md)
  A value that indicates if the key is pressed.
- [BEKeyEntry.KeyPressState](./keypressstate.md)
  Key-press states for a keyboard event.
- [var isKeyRepeating: Bool](./iskeyrepeating.md)
  A Boolean value that indicates whether the person holds a key down to repeat its key event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeyentry/timestamp)*