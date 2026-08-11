# inputTypes

**Framework**: Core Spotlight  
**Kind**: property  
**Required**: Yes

The data types this stage accepts as input.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var inputTypes: [SearchPipelineDataType] { get }
```

#### Discussion

Specify at least one input type for your stage. For each input type you specify, implement the corresponding `execute` method that accepts the input type.

The model considers your stage’s input types, output type, and other factors when determining whether to include the stage in a pipeline. When constructing the pipeline, the system maps the output from one stage to the input of the next.

## See Also

- [static var name: String](customstage/name.md)
  The name of the stage as you want it to appear in the pipeline.
- [static var description: String](customstage/description.md)
  A human-readable description of what this stage does.
- [static var outputType: SearchPipelineDataType](customstage/outputtype.md)
  The data type this stage produces as output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/customstage/inputtypes)*