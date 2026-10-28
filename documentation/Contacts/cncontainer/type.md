# type

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The type of the container.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var type: CNContainerType { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, readonly) CNContainerType type;
```

*macOS*

```objc
@property (atomic, readonly) CNContainerType type;
```

## Discussion

To learn more about different container types, see [`CNContainerType`](../cncontainertype.md).

## See Also

### Getting the Container Information
- [var name: String](./name.md)
  The name of the container.
- [var identifier: String](./identifier.md)
  The unique identifier for a contacts container on the device.
- [enum CNContainerType](../cncontainertype.md)
  The container may be local on the device or associated with a server account that has contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontainer/type)*