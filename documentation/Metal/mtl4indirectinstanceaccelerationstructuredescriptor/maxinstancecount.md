# maxInstanceCount

**Framework**: Metal  
**Kind**: property

Controls the maximum number of instance descriptors the instance descriptor buffer can reference.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var maxInstanceCount: Int { get set }
```

#### Discussion

You are responsible for ensuring that the final number of instances at build time, which you provide indirectly via a buffer reference in [`instanceCountBuffer`](mtl4indirectinstanceaccelerationstructuredescriptor/instancecountbuffer.md), is less than or equal to this number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/maxinstancecount)*