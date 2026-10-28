# init(uuid:name:)

**Framework**: HomeKit  
**Kind**: init  
**Role**: Initializer

Creates a structure that represents an accessory that was successfully transferred from a temporary home to a person’s home hub.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+

## Declaration

```swift
init(uuid: UUID, name: String)
```

## Return Value

An accessory that was successfully transferred to the home hub.

## Parameters

- `uuid`: A string that uniquely identifies an accessory.
- `name`: A string with the name of the accessory.

## See Also

### Describing the transferred accessory
- [var uuid: UUID](./uuid.md)
  A unique identifier for the accessory.
- [var name: String](./name.md)
  The name of the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmhome/provisionalhometransferresult/transferredaccessory/init(uuid:name:))*