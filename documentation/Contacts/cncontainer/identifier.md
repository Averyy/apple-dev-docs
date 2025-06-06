# identifier

**Framework**: Contacts  
**Kind**: property

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

#### Discussion

It is recommended that you use the identifier when re-fetching the container. The identifier can be persisted between app launches.

## See Also

- [var name: String](cncontainer/name.md)
  The name of the container.
- [var type: CNContainerType](cncontainer/type.md)
  The type of the container.
- [enum CNContainerType](cncontainertype.md)
  The container may be local on the device or associated with a server account that has contacts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/contacts/cncontainer/identifier)*