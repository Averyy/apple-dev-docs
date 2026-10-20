# shouldEvaluateForInputSystemHandling

**Framework**: BrowserEngineKit  
**Kind**: property  
**Role**: Instance Property

Represents whether the key event should be evaluated within the context of a composed input mode.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
var shouldEvaluateForInputSystemHandling: Bool { get set }
```

```objc
@property (nonatomic, assign, readwrite) BOOL shouldEvaluateForInputSystemHandling;
```

#### Discussion

When using an input mode with composed input, such as Chinese/Japanese/Korean, the markedText will be used to combine multiple key events into a single character.

## See Also

### Getting the information about the key event
- [var keyEntry: BEKeyEntry](./keyentry.md)
  BEKeyEntry for which this context is representing.
- [var shouldInsertCharacter: Bool](./shouldinsertcharacter.md)
  Represents whether a character should be inserted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeyentrycontext/shouldevaluateforinputsystemhandling)*