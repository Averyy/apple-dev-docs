# identifier

**Framework**: Contacts  
**Kind**: property  
**Role**: Instance Property

The unique identifier for a contacts container on the device.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var identifier: String { get }
```

*iOS, iPadOS, Mac Catalyst, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * identifier;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * identifier;
```

#### Discussion

It is recommended that you use the identifier when re-fetching the container. The identifier can be persisted between app launches.

## See Also

### Getting the Container Information
- [var name: String](./name.md)
  The name of the container.
- [var type: CNContainerType](./type.md)
  The type of the container.
- [enum CNContainerType](../cncontainertype.md)
  The container may be local on the device or associated with a server account that has contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontainer/identifier)*