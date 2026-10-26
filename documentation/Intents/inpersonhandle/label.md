# label

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

A standard label that describes the meaning of the information.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.1+

## Declaration

```swift
var label: INPersonHandleLabel? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, readonly, nullable) INPersonHandleLabel label;
```

*macOS*

```objc
@property (atomic, readonly, nullable) INPersonHandleLabel label;
```

#### Discussion

Use the value in this property to distinguish between person handles with similar types of information. For example, you might use it to distinguish between a person’s home and work phone numbers.

## See Also

### Getting the Handle Information
- [var type: INPersonHandleType](./type.md)
  The type of information contained in the handle.
- [var value: String?](./value.md)
  The data for the handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpersonhandle/label)*