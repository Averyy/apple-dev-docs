# reset()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method

Resets the default state for the vertex descriptor.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func reset()
```

```objc
- (void) reset;
```

## Discussion

After reset, each element of the [`attributes`](./attributes.md) array has a default vertex attribute descriptor, and each element of the [`layouts`](./layouts.md) array has a default vertex buffer layout descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexdescriptor/reset())*