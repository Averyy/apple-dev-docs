# kernelNames(fromMetalLibraryData:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Return an array of strings containing the names of all of the kernels contained in the Metal library.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
class func kernelNames(fromMetalLibraryData data: Data) -> [String]
```

```objc
+ (NSArray<NSString *> *) kernelNamesFromMetalLibraryData:(NSData *) data;
```

## Return Value

An Array of strings containing the names of the kernels.

## Parameters

- `data`: Contents of the Metal library.

## See Also

### Creating a Kernel Using Metal Shading Language
- [convenience init(functionName: String, fromMetalLibraryData: Data) throws](./init%28functionname,frommetallibrarydata%29.md)
  Creates a single kernel object using a Metal Shading Language (MSL) kernel function.
- [convenience init(functionName: String, fromMetalLibraryData: Data, outputPixelFormat: CIFormat) throws](./init%28functionname,frommetallibrarydata,outputpixelformat%29.md)
  Creates a single kernel object using a Metal Shading Language kernel function with optional pixel format.
- [class func kernels(withMetalString: String) throws -> [CIKernel]](./kernels%28withmetalstring%29.md)
  Load kernels from a Metal language string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/cikernel/kernelnames(frommetallibrarydata:))*