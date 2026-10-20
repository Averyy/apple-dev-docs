# kernels(withMetalString:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Load kernels from a Metal language string.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class func kernels(withMetalString source: String) throws -> [CIKernel]
```

```objc
+ (NSArray<CIKernel *> *) kernelsWithMetalString:(NSString *) source error:(NSError **) error;
```

#### Return Value

An array of [`CIKernel`](../cikernel.md) objects.

## Parameters

- `source`: A string containing the progam in Metal language.

## See Also

### Creating a Kernel Using Metal Shading Language
- [convenience init(functionName: String, fromMetalLibraryData: Data) throws](./init%28functionname,frommetallibrarydata%29.md)
  Creates a single kernel object using a Metal Shading Language (MSL) kernel function.
- [convenience init(functionName: String, fromMetalLibraryData: Data, outputPixelFormat: CIFormat) throws](./init%28functionname,frommetallibrarydata,outputpixelformat%29.md)
  Creates a single kernel object using a Metal Shading Language kernel function with optional pixel format.
- [class func kernelNames(fromMetalLibraryData: Data) -> [String]](./kernelnames%28frommetallibrarydata%29.md)
  Return an array of strings containing the names of all of the kernels contained in the Metal library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernel/kernels(withmetalstring:))*