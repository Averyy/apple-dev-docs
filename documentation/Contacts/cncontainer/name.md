# name

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The name of the container.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var name: String { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * name;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * name;
```

## See Also

### Getting the Container Information
- [var identifier: String](./identifier.md)
  The unique identifier for a contacts container on the device.
- [var type: CNContainerType](./type.md)
  The type of the container.
- [enum CNContainerType](../cncontainertype.md)
  The container may be local on the device or associated with a server account that has contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontainer/name)*