# offlineGPUCount()

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Returns the number of GPUs not currently driving a display.

**Availability**:
- macOS 10.10+

## Declaration

```swift
class func offlineGPUCount() -> UInt32
```

```objc
+ (unsigned int) offlineGPUCount;
```

#### Return Value

The number of offline GPU devices.

#### Discussion

If this count is greater than zero, the system has attached GPU devices that are not currently driving a display. You can use these devices for Core Image rendering by creating a context with the [`init(forOfflineGPUAtIndex:)`](./init%28forofflinegpuatindex%29.md) or[`init(forOfflineGPUAtIndex:colorSpace:options:sharedContext:)`](./init%28forofflinegpuatindex,colorspace,options,sharedcontext%29.md) method.

## See Also

### Managing Resources
- [func clearCaches()](./clearcaches%28%29.md)
  Frees any cached data, such as temporary images, associated with the context and runs the garbage collector.
- [func reclaimResources()](./reclaimresources%28%29.md)
  Runs the garbage collector to reclaim any resources that the context no longer requires.
- [var workingColorSpace: CGColorSpace?](./workingcolorspace.md)
  The working color space of the Core Image context.
- [var workingFormat: CIFormat](./workingformat.md)
  The working pixel format of the Core Image context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/offlinegpucount())*