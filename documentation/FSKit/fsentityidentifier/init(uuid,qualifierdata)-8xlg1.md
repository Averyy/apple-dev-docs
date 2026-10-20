# init(uuid:qualifierData:)

**Framework**: FSKit  
**Kind**: init  
**Role**: Initializer

Creates an entity identifier with the given UUID and qualifier data.

**Availability**:
- macOS 27.0+

## Declaration

```swift
init?(uuid: UUID, qualifierData: Data)
```

```objc
- (instancetype) initWithUUID:(NSUUID *) uuid qualifierData:(NSData *) qualifierData;
```

#### Return Value

A new identifier, or `nil` if `qualifierData` is not exactly eight bytes long.

## Parameters

- `uuid`: The UUID to use for this identifier.
- `qualifierData`: The data to distinguish entities that otherwise share the same UUID. Must be exactly eight bytes; any other length causes this initializer to return `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsentityidentifier/init(uuid:qualifierdata:)-8xlg1)*