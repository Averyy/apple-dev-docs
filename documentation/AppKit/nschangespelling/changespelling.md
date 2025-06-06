# changeSpelling(_:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Replaces the selected word in the receiver with a corrected version from the Spelling panel.

**Availability**:
- macOS ?+

## Declaration

```swift
func changeSpelling(_ sender: Any?)
```

#### Discussion

This message is sent by the `NSSpellChecker` to the object whose text is being checked. To get the corrected spelling, ask `sender` for the string value of its selected cell (visible to the user as the text field in the Spelling panel). This method should replace the selected portion of the text with the string that it gets from the NSSpellChecker.

## See Also

- [Spell Checking Programming Topics](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SpellCheck/SpellCheck.html#//apple_ref/doc/uid/10000092i)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nschangespelling/changespelling(_:))*