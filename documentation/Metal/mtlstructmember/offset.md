# offset

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The location of this member relative to the start of its struct, in bytes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var offset: Int { get }
```

```objc
@property (readonly) NSUInteger offset;
```

## See Also

### Describing the struct member
- [var name: String](./name.md)
  The name of the struct member.
- [var dataType: MTLDataType](./datatype.md)
  The data type of the struct member.
- [var argumentIndex: Int](./argumentindex.md)
  The index in the argument table that corresponds to the struct member.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstructmember/offset)*