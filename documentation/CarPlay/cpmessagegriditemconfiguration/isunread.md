# isUnread

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the conversation contains unread messages.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var isUnread: Bool { get set }
```

```objc
@property (nonatomic, getter=isUnread) BOOL unread;
```

## Discussion

The value of this property is `true` if the conversation contains unread messages, or `false` if it doesn’t.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpmessagegriditemconfiguration/isunread)*