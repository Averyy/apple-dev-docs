# messageTintColor

**Framework**: Messages  
**Kind**: property  
**Required**: Yes

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
var messageTintColor: UIColor? { get }
```

#### Discussion

This color will be drawn either in a material or as a solid color, depending on transcript context. The default value is nil, which renders the plugin balloon with the system standard background color. This must be a simple RGB color - other color types such as displayP3 or pattern images are not supported. This also does not support dynamic colors. If your color needs to be dynamic, you must call `invalidateMessageTintColor` when the dynamic conditions change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessagesapptranscriptpresentation/messagetintcolor)*