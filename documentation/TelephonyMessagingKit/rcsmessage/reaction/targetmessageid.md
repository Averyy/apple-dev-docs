# targetMessageID

**Framework**: TelephonyMessagingKit  
**Kind**: property

The target message ID for the reaction.

**Availability**:
- iOS 27.0+ (Beta)

## Declaration

```swift
var targetMessageID: RCSMessageID
```

#### Discussion

When adding a reaction, this property indicates the target message ID for the reaction. Your app should store the message ID for the sent message used to add the reaction. This is necessary for removing the reaction at a later point in time.

When removing a reaction, this identifier indicates the message ID previously used when adding a reaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsmessage/reaction/targetmessageid)*