# targetMessageID

**Framework**: TelephonyMessagingKit  
**Kind**: property

The target message ID for the custom reaction.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)

## Declaration

```swift
var targetMessageID: RCSMessageID
```

#### Discussion

When adding a custom reaction, this property indicates the target message ID for the custom reaction. Your app should store the message ID for the sent message used to add the custom reaction. This is necessary for removing the custom reaction at a later point in time.

When removing a custom reaction, this identifier indicates the message ID previously used when adding a custom reaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/customreaction/targetmessageid)*