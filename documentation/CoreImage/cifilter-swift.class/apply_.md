# apply:

**Framework**: Core Image  
**Kind**: method  
**Role**: Instance Method

Produces a [`CIImage`](../ciimage.md) object by applying a kernel function.

**Availability**:
- macOS 10.4+

## Declaration

```objc
- (CIImage *) apply:(CIKernel *) k;
```

## Discussion

If you are implementing a custom filter, this method needs to be called from within the [`outputImage`](./outputimage.md) method in order to apply your kernel function to the [`CIImage`](../ciimage.md) object. For example, if the kernel function has this signature:

```objc
kernel vec4 brightenEffect (sampler src, float k)
```

You would supply two arguments after the `k` argument  to the `apply:k, ...` method. In this case, the first argument must be a sampler and the second a floating-point value. For more information on kernels, see [Core Image Kernel Language Reference](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Reference/CIKernelLangRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004397).

## Parameters

- `k`: A [`CIKernel`](../cikernel.md) object that contains a kernel function.

## See Also

### Applying a filter
- [func apply(CIKernel, arguments: [Any]?, options: [String : Any]?) -> CIImage?](./apply%28_,arguments,options%29.md)
  Produces a [`CIImage`](../ciimage.md) object by applying arguments to a kernel function and using options to control how the kernel function is evaluated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cifilter-swift.class/apply:)*