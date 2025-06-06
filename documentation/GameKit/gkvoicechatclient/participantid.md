# participantID()

**Framework**: GameKit  
**Kind**: method  
**Required**: Yes

Returns a string that uniquely identifies the local user.

**Availability**:
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func participantID() -> String
```

#### Return Value

A string that can be used by other participants to connect to the local user.

#### Discussion

The client decides the format and meaning of the participant identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/participantid())*