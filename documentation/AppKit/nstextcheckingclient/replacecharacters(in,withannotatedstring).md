# replaceCharacters(in:withAnnotatedString:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS 10.0+

## Declaration

```swift
func replaceCharacters(in range: NSRange, withAnnotatedString annotatedString: NSAttributedString)
```

```objc
- (void) replaceCharactersInRange:(NSRange) range withAnnotatedString:(NSAttributedString *) annotatedString;
```

## See Also

### Instance Methods
- [func addAnnotations([NSAttributedString.Key : String], range: NSRange)](./addannotations%28_,range%29.md)
- [func annotatedSubstring(forProposedRange: NSRange, actualRange: NSRangePointer?) -> NSAttributedString?](./annotatedsubstring%28forproposedrange,actualrange%29.md)
- [func candidateListTouchBarItem() -> NSCandidateListTouchBarItem<AnyObject>?](./candidatelisttouchbaritem%28%29.md)
- [func removeAnnotation(NSAttributedString.Key, range: NSRange)](./removeannotation%28_,range%29.md)
- [func selectAndShow(NSRange)](./selectandshow%28_%29.md)
- [func setAnnotations([NSAttributedString.Key : String], range: NSRange)](./setannotations%28_,range%29.md)
- [func view(for: NSRange, firstRect: NSRectPointer?, actualRange: NSRangePointer?) -> NSView?](./view%28for,firstrect,actualrange%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcheckingclient/replacecharacters(in:withannotatedstring:))*