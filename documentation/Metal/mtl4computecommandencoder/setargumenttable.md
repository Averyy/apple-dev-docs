# setArgumentTable(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets an argument table for the compute shader stage of this pipeline.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setArgumentTable(_ argumentTable: (any MTL4ArgumentTable)?)
```

#### Discussion

Metal takes a snapshot of the resources in the argument table when you make dispatch or execute calls on this encoder instance. Metal makes the snapshot contents available to the compute shader function of the current pipeline state.

## Parameters

- `argumentTable`: A   to set on the command encoder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computecommandencoder/setargumenttable(_:))*