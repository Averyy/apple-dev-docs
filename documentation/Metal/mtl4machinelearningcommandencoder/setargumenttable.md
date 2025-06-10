# setArgumentTable(_:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Sets an argument table for the command encoder’s machine learning shader stage.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func setArgumentTable(_ argumentTable: any MTL4ArgumentTable)
```

#### Discussion

The argument table provides inputs to all subsequent Machine Learning dispatches.

## Parameters

- `argumentTable`: An argument table to set on the command encoder’s Machine Learning stage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4machinelearningcommandencoder/setargumenttable(_:))*