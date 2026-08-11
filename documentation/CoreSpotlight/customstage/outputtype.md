# outputType

**Framework**: Core Spotlight  
**Kind**: property  
**Required**: Yes

The data type this stage produces as output.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var outputType: SearchPipelineDataType { get }
```

#### Discussion

Specify the type of data your custom stage supports. In the implementation of your type’s `execute` methods, generate a [`SearchPipelineData`](searchpipelinedata.md) structure with the type of data you specified in this property.

The model considers your stage’s input types, output type, and other factors when determining whether to include the stage in a pipeline. When constructing the pipeline, the system maps the output from one stage to the input of the next.

## See Also

- [static var name: String](customstage/name.md)
  The name of the stage as you want it to appear in the pipeline.
- [static var description: String](customstage/description.md)
  A human-readable description of what this stage does.
- [static var inputTypes: [SearchPipelineDataType]](customstage/inputtypes.md)
  The data types this stage accepts as input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/customstage/outputtype)*