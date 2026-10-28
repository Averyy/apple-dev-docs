# flags

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

A collection of environmental effects to include in the output.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var flags: PHASESpatialPipeline.Flags { get }
```

```objc
@property (nonatomic, readonly) PHASESpatialPipelineFlags flags;
```

## Discussion

The framework sets the value of this property to the [`init(flags:)`](./init%28flags%29.md) argument.

## See Also

### Inspecting Effects
- [var entries: [PHASESpatialCategory : PHASESpatialPipelineEntry]](./entries.md)
  Audio layers for environmental effects to add to the output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasespatialpipeline/flags-swift.property)*