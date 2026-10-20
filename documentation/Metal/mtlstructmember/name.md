# name

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The name of the struct member.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var name: String { get }
```

```objc
@property (readonly) NSString * name;
```

## See Also

### Related Documentation
- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
### Describing the struct member
- [var dataType: MTLDataType](./datatype.md)
  The data type of the struct member.
- [var offset: Int](./offset.md)
  The location of this member relative to the start of its struct, in bytes.
- [var argumentIndex: Int](./argumentindex.md)
  The index in the argument table that corresponds to the struct member.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstructmember/name)*