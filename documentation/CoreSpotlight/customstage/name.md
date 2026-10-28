# name

**Framework**: Core Spotlight  
**Kind**: property  
**Role**: Type Property  
**Required**: Yes

The name of the stage as you want it to appear in the pipeline.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
static var name: String { get }
```

## Discussion

Keep stage names simple and descriptive, and don’t use the same stage name for multiple custom stage types.

## See Also

### Getting the stage metadata
- [static var description: String](./description.md)
  A human-readable description of what this stage does.
- [static var inputTypes: [SearchPipelineDataType]](./inputtypes.md)
  The data types this stage accepts as input.
- [static var outputType: SearchPipelineDataType](./outputtype.md)
  The data type this stage produces as output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/customstage/name)*