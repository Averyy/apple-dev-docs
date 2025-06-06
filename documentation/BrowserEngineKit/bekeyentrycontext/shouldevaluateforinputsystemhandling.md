# shouldEvaluateForInputSystemHandling

**Framework**: BrowserEngineKit  
**Kind**: property

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

#### Discussion

When using an input mode with composed input, such as Chinese/Japanese/Korean, the markedText will be used to combine multiple key events into a single character.

## See Also

- [var keyEntry: BEKeyEntry](bekeyentrycontext/keyentry.md)
  BEKeyEntry for which this context is representing.
- [var shouldInsertCharacter: Bool](bekeyentrycontext/shouldinsertcharacter.md)
  Represents whether a character should be inserted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bekeyentrycontext/shouldevaluateforinputsystemhandling)*