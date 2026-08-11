# name

**Framework**: Core Spotlight  
**Kind**: property  
**Required**: Yes

The name of the stage as you want it to appear in the pipeline.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var name: String { get }
```

#### Discussion

Keep stage names simple and descriptive, and don’t use the same stage name for multiple custom stage types.

## See Also

- [static var description: String](customstage/description.md)
  A human-readable description of what this stage does.
- [static var inputTypes: [SearchPipelineDataType]](customstage/inputtypes.md)
  The data types this stage accepts as input.
- [static var outputType: SearchPipelineDataType](customstage/outputtype.md)
  The data type this stage produces as output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/customstage/name)*