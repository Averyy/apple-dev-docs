# ignoreSpelling(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS

## Declaration

```swift
func ignoreSpelling(_ sender: Any?)
```

```objc
- (void) ignoreSpelling:(id) sender;
```

## Discussion

Implement this action method to allow an application to ignore misspelled words on a document-by-document basis. This message is sent by the NSSpellChecker instance to the object whose text is being checked.

Implement this method by using the code shown in the protocol description.

## See Also

### Related Documentation
- [Spell Checking Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SpellCheck/SpellCheck.html#//apple_ref/doc/uid/10000092i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsignoremisspelledwords/ignorespelling(_:))*