# init(groupName:groupId:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates a call record with the group details.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- visionOS 1.0+
- watchOS 7.3+

## Declaration

```swift
init(groupName: String?, groupId: String?)
```

```objc
- (instancetype) initWithGroupName:(NSString *) groupName groupId:(NSString *) groupId;
```

## Return Value

An initialized [`INCallGroup`](../incallgroup.md) object or `nil` if the user did not initialize the object.

## Parameters

- `groupName`: The name contributed the user to their group call. This field can be `nil`.
- `groupId`: A unique identifier that disguishes call groups. This field can be `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incallgroup/init(groupname:groupid:))*