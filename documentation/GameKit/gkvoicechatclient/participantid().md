# participantID()

**Framework**: GameKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns a string that uniquely identifies the local user.

**Availability**:
- iOS 3.0+ - Deprecated in 7.0
- iPadOS 3.0+ - Deprecated in 7.0
- Mac Catalyst 3.0+ - Deprecated in 7.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 3.0

## Declaration

```swift
func participantID() -> String
```

```objc
- (NSString *) participantID;
```

#### Return Value

A string that can be used by other participants to connect to the local user.

#### Discussion

The client decides the format and meaning of the participant identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkvoicechatclient/participantid())*