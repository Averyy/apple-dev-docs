# setAnnotations(_:range:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- macOS 10.0+

## Declaration

```swift
func setAnnotations(_ annotations: [NSAttributedString.Key : String], range: NSRange)
```

```objc
- (void) setAnnotations:(NSDictionary<NSString *,NSString *> *) annotations range:(NSRange) range;
```

## See Also

### Instance Methods
- [func addAnnotations([NSAttributedString.Key : String], range: NSRange)](./addannotations%28_,range%29.md)
- [func annotatedSubstring(forProposedRange: NSRange, actualRange: NSRangePointer?) -> NSAttributedString?](./annotatedsubstring%28forproposedrange,actualrange%29.md)
- [func candidateListTouchBarItem() -> NSCandidateListTouchBarItem<AnyObject>?](./candidatelisttouchbaritem%28%29.md)
- [func removeAnnotation(NSAttributedString.Key, range: NSRange)](./removeannotation%28_,range%29.md)
- [func replaceCharacters(in: NSRange, withAnnotatedString: NSAttributedString)](./replacecharacters%28in,withannotatedstring%29.md)
- [func selectAndShow(NSRange)](./selectandshow%28_%29.md)
- [func view(for: NSRange, firstRect: NSRectPointer?, actualRange: NSRangePointer?) -> NSView?](./view%28for,firstrect,actualrange%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcheckingclient/setannotations(_:range:))*