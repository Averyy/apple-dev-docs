# qualifier

**Framework**: FSKit  
**Kind**: property  
**Role**: Instance Property

An optional piece of data to distinguish entities that otherwise share the same UUID.

**Availability**:
- macOS 15.4+

## Declaration

```swift
var qualifier: Data? { get set }
```

```objc
@property (copy, nullable) NSData * qualifier;
```

## See Also

### Inspecting identifier properties
- [var uuid: UUID](./uuid.md)
  A UUID to uniquely identify this entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsentityidentifier/qualifier)*