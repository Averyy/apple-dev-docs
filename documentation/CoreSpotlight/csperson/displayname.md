# displayName

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Instance Property

A display name for the person.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var displayName: String? { get }
```

```objc
@property (readonly, nullable) NSString * displayName;
```

## Discussion

Use this optional property to provide a name for the person object that can be displayed to users.

## See Also

### Accessing person properties
- [var contactIdentifier: String?](./contactidentifier.md)
  The identifier for the contact associated with the person.
- [var handleIdentifier: String](./handleidentifier.md)
  A key that identifies the type of contact property represented by the person object’s handle.
- [var handles: [String]](./handles.md)
  An array of contact handles related to the person.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/csperson/displayname)*