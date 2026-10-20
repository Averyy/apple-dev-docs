# maximumActionButtonCount

**Framework**: CarPlay  
**Kind**: property  
**Role**: Type Property

The maximum number of action buttons that can be displayed in the CPVoiceControlTemplate.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
class var maximumActionButtonCount: Int { get }
```

```objc
@property (class, nonatomic, readonly) NSInteger maximumActionButtonCount;
```

#### Return Value

The maximum number of action buttons supported by this template.

#### Discussion

This class property defines the upper limit for action buttons to ensure proper layout and usability within the CarPlay interface constraints. Any buttons beyond this limit in the actionButtons array will be ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpvoicecontrolstate/maximumactionbuttoncount)*