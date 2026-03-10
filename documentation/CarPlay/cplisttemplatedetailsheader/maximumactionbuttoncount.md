# maximumActionButtonCount

**Framework**: CarPlay  
**Kind**: property

The maximum number of action buttons that can be displayed in the header.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
class var maximumActionButtonCount: Int { get }
```

#### Return Value

The maximum number of action buttons supported by this header type.

#### Discussion

This class property defines the upper limit for action buttons to ensure proper layout and usability within the CarPlay interface constraints. Any buttons beyond this limit in the actionButtons array will be ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplisttemplatedetailsheader/maximumactionbuttoncount)*