# accessibilityCustomRotors

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The custom rotors of the current accessibility element.

**Availability**:
- macOS 10.13+

## Declaration

```objc
@property (copy) NSArray<NSAccessibilityCustomRotor *> * accessibilityCustomRotors;
```

#### Discussion

Custom rotors are lists of items of a specific category. For example, a “headings” rotor returns a list of headings a given document.

## See Also

### Assigning rotors
- [class NSAccessibilityCustomRotor](../nsaccessibilitycustomrotor.md)
  A context-sensitive function that helps VoiceOver users find the next instance of a related accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsaccessibility-c.protocol/accessibilitycustomrotors)*