# description

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

A human-readable description of what this stage does.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static var description: String { get }
```

## Mentions

- [Making your indexed content available to Foundation Models](../making-your-indexed-content-available-to-foundation-models.md)

## Discussion

The model uses the value in this property as instructions on how to use the stage.

## See Also

### Getting the stage metadata
- [static var name: String](./name.md)
  The name of the stage as you want it to appear in the pipeline.
- [static var inputTypes: [SearchPipelineDataType]](./inputtypes.md)
  The data types this stage accepts as input.
- [static var outputType: SearchPipelineDataType](./outputtype.md)
  The data type this stage produces as output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/customstage/description)*