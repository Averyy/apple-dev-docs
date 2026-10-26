# layer

**Framework**: Core Animation  
**Kind**: method  
**Role**: Type Method

Creates and returns an instance of the layer object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) layer;
```

#### Return Value

The initialized layer object or `nil` if initialization was not successful.

#### Discussion

If you subclass `CALayer`, you may override this method and use it to provide an instance of your specific subclass.

## See Also

### Related Documentation
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
### Creating a layer
- [init()](./init%28%29.md)
  Returns an initialized `CALayer` object.
- [init(layer: Any)](./init%28layer%29.md)
  Override to copy or initialize custom fields of the specified layer.
- [init(remoteClientId: UInt32)](./init%28remoteclientid%29.md)
  Initializes a layer with a remote client ID.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/layer)*