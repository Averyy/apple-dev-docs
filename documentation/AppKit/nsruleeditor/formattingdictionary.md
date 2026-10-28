# formattingDictionary

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The formatting dictionary for the rule editor.

**Availability**:
- macOS

## Declaration

```swift
var formattingDictionary: [String : String]? { get set }
```

```objc
@property (copy, nullable) NSDictionary<NSString *,NSString *> * formattingDictionary;
```

## Discussion

If you assign a new the formatting dictionary to this property, it sets the current to formatting strings file name to `nil`.

## See Also

### Working with Formatting
- [var formattingStringsFilename: String?](./formattingstringsfilename.md)
  The name of the rule editor’s strings file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsruleeditor/formattingdictionary)*