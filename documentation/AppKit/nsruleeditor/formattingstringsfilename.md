# formattingStringsFilename

**Framework**: AppKit  
**Kind**: property

The name of the rule editor’s strings file.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var formattingStringsFilename: String? { get set }
```

#### Discussion

The `NSRuleEditor` class looks for a strings file with the given name in the main bundle and (if appropriate) the bundle containing the nib file from which it was loaded. If it finds a strings file resource with the given name, `NSRuleEditor` loads it and sets it as the formatting dictionary for the receiver. You can obtain the resulting dictionary using the [`formattingDictionary`](nsruleeditor/formattingdictionary.md) property].

If you assign a new dictionary to the [`formattingDictionary`](nsruleeditor/formattingdictionary.md) property, it sets the current to formatting strings file name to `nil`.

## See Also

- [var formattingDictionary: [String : String]?](nsruleeditor/formattingdictionary.md)
  The formatting dictionary for the rule editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/formattingstringsfilename)*