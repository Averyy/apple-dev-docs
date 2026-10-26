# displayName

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The person’s formatted name.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var displayName: String { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) NSString * displayName;
```

*macOS*

```objc
@property (atomic, copy, readonly) NSString * displayName;
```

#### Discussion

This property contains the name components specified at initialization time. Use the information in this property or the [`nameComponents`](./namecomponents.md) property to identify the name of the user.

## See Also

### Accessing the name
- [var nameComponents: PersonNameComponents?](./namecomponents.md)
  The individual components of the person’s full name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inperson/displayname)*