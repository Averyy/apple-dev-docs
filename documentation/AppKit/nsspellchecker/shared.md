# shared

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Returns the NSSpellChecker (one per application).

**Availability**:
- macOS

## Declaration

```swift
class var shared: NSSpellChecker { get }
```

```objc
@property (class, strong, readonly) NSSpellChecker * sharedSpellChecker;
```

#### Return Value

The spelling checker shared by this application.

## See Also

### Related Documentation
- [Spell Checking Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SpellCheck/SpellCheck.html#//apple_ref/doc/uid/10000092i)
### Getting the Spell Checker
- [class var sharedSpellCheckerExists: Bool](./sharedspellcheckerexists.md)
  Returns whether the application’s NSSpellChecker has already been created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsspellchecker/shared)*