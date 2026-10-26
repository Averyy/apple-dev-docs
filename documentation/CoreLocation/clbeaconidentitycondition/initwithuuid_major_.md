# initWithUUID:major:

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Creates a new beacon identity condition with the identifier and major value you specify.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
- (instancetype) initWithUUID:(NSUUID *) uuid major:(CLBeaconMajorValue) major;
```

## Parameters

- `uuid`: A [`UUID`](./uuid.md) to use as the beacon’s identifier.
- `major`: A [`CLBeaconMajorValue`](../clbeaconmajorvalue.md) to use as the beacon’s major value.

## See Also

### Creating beacon identity conditions
- [- initWithUUID:](./initwithuuid_.md)
  Creates a new beacon identity condition with the identifier you specify.
- [- initWithUUID:major:minor:](./initwithuuid_major_minor_.md)
  Creates a new beacon identity condition with the identifier, and major and minor values you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeaconidentitycondition/initwithuuid:major:)*