# NSTextCheckingClient

**Framework**: AppKit  
**Kind**: protocol

**Availability**:
- macOS ?+

## Declaration

```swift
protocol NSTextCheckingClient : NSTextInputClient, NSTextInputTraits
```

## Topics

### Instance Methods
- [func addAnnotations([NSAttributedString.Key : String], range: NSRange)](nstextcheckingclient/addannotations(_:range:).md)
- [func annotatedSubstring(forProposedRange: NSRange, actualRange: NSRangePointer?) -> NSAttributedString?](nstextcheckingclient/annotatedsubstring(forproposedrange:actualrange:).md)
- [func candidateListTouchBarItem() -> NSCandidateListTouchBarItem<AnyObject>?](nstextcheckingclient/candidatelisttouchbaritem.md)
- [func removeAnnotation(NSAttributedString.Key, range: NSRange)](nstextcheckingclient/removeannotation(_:range:).md)
- [func replaceCharacters(in: NSRange, withAnnotatedString: NSAttributedString)](nstextcheckingclient/replacecharacters(in:withannotatedstring:).md)
- [func selectAndShow(NSRange)](nstextcheckingclient/selectandshow(_:).md)
- [func setAnnotations([NSAttributedString.Key : String], range: NSRange)](nstextcheckingclient/setannotations(_:range:).md)
- [func view(for: NSRange, firstRect: NSRectPointer?, actualRange: NSRangePointer?) -> NSView?](nstextcheckingclient/view(for:firstrect:actualrange:).md)

## Relationships

### Inherits From
- [NSTextInputClient](nstextinputclient.md)
- [NSTextInputTraits](nstextinputtraits.md)

## See Also

- [class NSTextCheckingController](nstextcheckingcontroller.md)
- [protocol NSTextInputTraits](nstextinputtraits.md)
- [enum NSTextInputTraitType](nstextinputtraittype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcheckingclient)*