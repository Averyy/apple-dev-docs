# run()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Causes the receiver to start listening for spell-checking requests.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func run()
```

```objc
- (void) run;
```

## Discussion

This method starts a loop that never returns; you need to set the `NSSpellServer` object’s delegate before sending this message.

## See Also

### Related Documentation
- [var delegate: (any NSSpellServerDelegate)?](./delegate.md)
  Returns the receiver’s delegate.
### Providing Spelling Services
- [func registerLanguage(String?, byVendor: String?) -> Bool](./registerlanguage%28_,byvendor%29.md)
  Notifies the receiver of a language your spelling checker can check.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsspellserver/run())*