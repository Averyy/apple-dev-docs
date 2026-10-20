# NSTextCheckingClient

**Framework**: AppKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- macOS

## Declaration

```swift
protocol NSTextCheckingClient : NSTextInputClient, NSTextInputTraits
```

```objc
@protocol NSTextCheckingClient <NSTextInputClient, NSTextInputTraits>
```

## Topics

### Instance Methods
- [func addAnnotations([NSAttributedString.Key : String], range: NSRange)](./nstextcheckingclient/addannotations%28_,range%29.md)
- [func annotatedSubstring(forProposedRange: NSRange, actualRange: NSRangePointer?) -> NSAttributedString?](./nstextcheckingclient/annotatedsubstring%28forproposedrange,actualrange%29.md)
- [func candidateListTouchBarItem() -> NSCandidateListTouchBarItem<AnyObject>?](./nstextcheckingclient/candidatelisttouchbaritem%28%29.md)
- [func removeAnnotation(NSAttributedString.Key, range: NSRange)](./nstextcheckingclient/removeannotation%28_,range%29.md)
- [func replaceCharacters(in: NSRange, withAnnotatedString: NSAttributedString)](./nstextcheckingclient/replacecharacters%28in,withannotatedstring%29.md)
- [func selectAndShow(NSRange)](./nstextcheckingclient/selectandshow%28_%29.md)
- [func setAnnotations([NSAttributedString.Key : String], range: NSRange)](./nstextcheckingclient/setannotations%28_,range%29.md)
- [func view(for: NSRange, firstRect: NSRectPointer?, actualRange: NSRangePointer?) -> NSView?](./nstextcheckingclient/view%28for,firstrect,actualrange%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTextInputClient](./nstextinputclient.md)
- [NSTextInputTraits](./nstextinputtraits.md)

## See Also

### Text-checking
- [class NSTextCheckingController](./nstextcheckingcontroller.md)
- [protocol NSTextInputTraits](./nstextinputtraits.md)
- [enum NSTextInputTraitType](./nstextinputtraittype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextcheckingclient)*