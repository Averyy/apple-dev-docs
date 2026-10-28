# value

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The data for the handle.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var value: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * value;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * value;
```

## Discussion

The contents of this property are determined by the value of the [`type`](./type.md) property. For example, when the handle specifies an email address, this property should contain a string similar to “address@example.com” describing the user’s email address. This information may be displayed to the user to help resolve the identity of the intended person.

## See Also

### Getting the Handle Information
- [var type: INPersonHandleType](./type.md)
  The type of information contained in the handle.
- [var label: INPersonHandleLabel?](./label.md)
  A standard label that describes the meaning of the information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpersonhandle/value)*