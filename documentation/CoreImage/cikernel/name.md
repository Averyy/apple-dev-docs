# name

**Framework**: Core Image  
**Kind**: property

The name of the kernel routine.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var name: String { get }
```

#### Discussion

The name of a kernel routine is the identifier used to declare it in the Core Image Kernel Language source code. For example, if you use the [`init(source:)`](cikernel/init(source:).md) method to create a kernel from the source code below, the name of the returned [`CIKernel`](cikernel.md) object is “moveUpTwoPixels”.

```objc
kernel vec4 moveUpTwoPixels (sampler image) {
    vec2 dc = destCoord();
    vec2 offset = vec2(0.0, 2.0);
    return sample (image, samplerTransform (image, dc + offset));
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernel/name)*