# sharedSpellCheckerExists

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns whether the application’s NSSpellChecker has already been created.

**Availability**:
- macOS

## Declaration

```swift
class var sharedSpellCheckerExists: Bool { get }
```

```objc
@property (class, readonly) BOOL sharedSpellCheckerExists;
```

## Return Value

[`true`](../../Swift/true.md) if the shared spell checker already exists, otherwise [`false`](../../Swift/false.md).

## See Also

### Getting the Spell Checker
- [class var shared: NSSpellChecker](./shared.md)
  Returns the NSSpellChecker (one per application).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/sharedspellcheckerexists)*