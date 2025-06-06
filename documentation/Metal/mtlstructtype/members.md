# members

**Framework**: Metal  
**Kind**: property

An array of objects that describe the fields in the struct.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var members: [MTLStructMember] { get }
```

#### Discussion

Each array element in [`members`](mtlstructtype/members.md) is a [`MTLStructMember`](mtlstructmember.md) object that corresponds to one of the fields in the struct.

## See Also

- [Metal Shading Language Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)
- [func memberByName(String) -> MTLStructMember?](mtlstructtype/memberbyname(_:).md)
  Provides a representation of a struct member.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlstructtype/members)*