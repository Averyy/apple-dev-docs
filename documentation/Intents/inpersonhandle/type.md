# type

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The type of information contained in the handle.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
var type: INPersonHandleType { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly) INPersonHandleType type;
```

*macOS*

```objc
@property (atomic, readonly) INPersonHandleType type;
```

#### Discussion

Use the value of this property to determine how to interpret the contents of the [`value`](./value.md) property.

## See Also

### Getting the Handle Information
- [var value: String?](./value.md)
  The data for the handle.
- [var label: INPersonHandleLabel?](./label.md)
  A standard label that describes the meaning of the information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpersonhandle/type)*