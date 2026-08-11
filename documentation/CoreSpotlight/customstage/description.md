# description

**Framework**: Core Spotlight  
**Kind**: property  
**Required**: Yes

A human-readable description of what this stage does.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var description: String { get }
```

## Mentions

- [Making your indexed content available to Foundation Models](making-your-indexed-content-available-to-foundation-models.md)

#### Discussion

The model uses the value in this property as instructions on how to use the stage.

## See Also

- [static var name: String](customstage/name.md)
  The name of the stage as you want it to appear in the pipeline.
- [static var inputTypes: [SearchPipelineDataType]](customstage/inputtypes.md)
  The data types this stage accepts as input.
- [static var outputType: SearchPipelineDataType](customstage/outputtype.md)
  The data type this stage produces as output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/customstage/description)*