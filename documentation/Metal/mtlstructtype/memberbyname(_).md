# memberByName(_:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Provides a representation of a struct member.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func memberByName(_ name: String) -> MTLStructMember?
```

```objc
- (MTLStructMember *) memberByName:(NSString *) name;
```

#### Return Value

An object that represents the named struct member. If `name` does not match a member name, `nil` is returned.

## Parameters

- `name`: The name of a member in the struct.

## See Also

### Obtaining information about struct members
- [var members: [MTLStructMember]](./members.md)
  An array of instances that describe the fields in the struct.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstructtype/memberbyname(_:))*