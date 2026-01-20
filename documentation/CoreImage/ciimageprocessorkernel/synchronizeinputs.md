# synchronizeInputs

**Framework**: Core Image  
**Kind**: property

Override this class property to return false if you want your processor to be given input objects that have not been synchronized for CPU access.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class var synchronizeInputs: Bool { get }
```

#### Discussion

Generally, if your subclass uses the GPU your should override this method to return false. If not overridden, true is returned.

## See Also

- [class var outputFormat: CIFormat](ciimageprocessorkernel/outputformat.md)
  Override this class property if you want your processor’s output to be in a specific pixel format.
- [class var outputIsOpaque: Bool](ciimageprocessorkernel/outputisopaque.md)
  Override this class property if your processor’s output stores 1.0 into the alpha channel of all pixels within the output extent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/synchronizeinputs)*