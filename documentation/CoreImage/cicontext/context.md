# context

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Creates a context without a specific rendering destination, using default options.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+

## Declaration

```objc
+ (CIContext *) context;
```

#### Return Value

A new Core Image context.

#### Discussion

If you create a context without specifying a rendering destination, Core Image automatically chooses and internally manages a rendering destination based on the current device’s capabilities. You cannot use a context without an explicit destination for the methods listed in Drawing Images. Instead, use the methods listed in Rendering Images.

To specify additional options for the context, use the [`contextWithOptions:`](./contextwithoptions_.md) method instead.

## See Also

### Related Documentation
- [Image Unit Tutorial](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/ImageUnitTutorial/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004531)
- [Core Image Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/CoreImaging/ci_intro/ci_intro.html#//apple_ref/doc/uid/TP30001185)
### Creating a Context Without Specifying a Destination
- [init()](./init%28%29.md)
  Initializes a context without a specific rendering destination, using default options.
- [+ contextWithOptions:](./contextwithoptions_.md)
  Initializes a context without a specific rendering destination, using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cicontext/context)*