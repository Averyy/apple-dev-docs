# alternateLayout

**Framework**: Messages  
**Kind**: property

A template layout to be displayed when the live layout is unavailable.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var alternateLayout: MSMessageTemplateLayout { get }
```

#### Discussion

To display the live layout, the device must be running iOS 11 or later, and must have your iMessage app installed. All other devices, including devices that do not support iMessage apps (macOS, iOS 9 and earlier, and SMS devices), use the  alternate layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagelivelayout/alternatelayout)*