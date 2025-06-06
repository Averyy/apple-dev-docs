# getOutputTypes(with:inputTypes:compilationDescriptor:)

**Framework**: Metal Performance Shaders Graph  
**Kind**: method

Get output shapes for a specialized executable.

**Availability**:
- iOS 16.3+
- iPadOS 16.3+
- Mac Catalyst 16.3+
- macOS 13.2+
- tvOS 16.3+
- visionOS 1.0+

## Declaration

```swift
func getOutputTypes(with device: MPSGraphDevice?, inputTypes: [MPSGraphType], compilationDescriptor: MPSGraphCompilationDescriptor?) -> [MPSGraphShapedType]?
```

#### Discussion

In case specialization has not been done yet then calling this function will specialize for the given input shapes.

## Parameters

- `device`: Optional MPSGraph device to compile with
- `inputTypes`: Input types expected to be passed to the executable.
- `compilationDescriptor`: CompilationDescriptor to be used to specialize, since the executable was created with a compilationDescriptor already this one overrides those settings to the extent it can.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshadersgraph/mpsgraphexecutable/getoutputtypes(with:inputtypes:compilationdescriptor:))*