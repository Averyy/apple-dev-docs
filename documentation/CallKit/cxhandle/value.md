# value

**Framework**: CallKit  
**Kind**: property  
**Role**: Instance Property

The value of the handle.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var value: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * value;
```

#### Discussion

A handle’s value corresponds to its type. For example, a handle with [`type`](./type.md) equal to [`CXHandle.HandleType.phoneNumber`](./handletype/phonenumber.md) should have a [`value`](./value.md) consisting of a sequence of digits.

## See Also

### Accessing Handle Attributes
- [var type: CXHandle.HandleType](./type.md)
  The type of the handle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/callkit/cxhandle/value)*