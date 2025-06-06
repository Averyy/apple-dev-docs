# run()

**Framework**: Foundation  
**Kind**: method

Causes the receiver to start listening for spell-checking requests.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func run()
```

#### Discussion

This method starts a loop that never returns; you need to set the `NSSpellServer` object’s delegate before sending this message.

## See Also

- [var delegate: (any NSSpellServerDelegate)?](nsspellserver/delegate.md)
  Returns the receiver’s delegate.
- [func registerLanguage(String?, byVendor: String?) -> Bool](nsspellserver/registerlanguage(_:byvendor:).md)
  Notifies the receiver of a language your spelling checker can check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspellserver/run())*