# objectFunctionDescriptor

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Assigns a function descriptor representing the function this pipeline executes for each *object* in the object shader stage.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@NSCopying
var objectFunctionDescriptor: MTL4FunctionDescriptor? { get set }
```

```objc
@property (nonatomic, copy, readwrite, nullable) MTL4FunctionDescriptor * objectFunctionDescriptor;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/objectfunctiondescriptor)*