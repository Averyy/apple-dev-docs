# clearCaches()

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func clearCaches()
```

```objc
- (void) clearCaches;
```

#### Discussion

You can use this method to remove textures from the texture cache that reference deleted images.

## See Also

### Managing Resources
- [func reclaimResources()](./reclaimresources%28%29.md)
  Runs the garbage collector to reclaim any resources that the context no longer requires.
- [class func offlineGPUCount() -> UInt32](./offlinegpucount%28%29.md)
  Returns the number of GPUs not currently driving a display.
- [var workingColorSpace: CGColorSpace?](./workingcolorspace.md)
  The working color space of the Core Image context.
- [var workingFormat: CIFormat](./workingformat.md)
  The working pixel format of the Core Image context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/clearcaches())*