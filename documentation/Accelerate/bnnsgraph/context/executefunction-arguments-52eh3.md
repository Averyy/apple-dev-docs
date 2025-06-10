# executeFunction(_:arguments:)

**Framework**: Accelerate  
**Kind**: method

Synchronously executes the specified function with the provided context.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func executeFunction(_ function: String? = nil, arguments: inout [BNNSTensor]) throws
```

#### Discussion

If the underlying model contains dynamic shaped inputs or outputs, these must be set prior to calling this routine through a call to either `setDynamicShapes(_:forFunction:)` or `setBatchSize(_:forFunction:)`. Don’t modify the shapes again until this routine has returned.

The same context must only be used by a single thread at a time.

> **Note**: `BNNSGraphContextExecute`

## Parameters

- `function`: The specific function to execute. You may set this to   if there is only one function.
- `arguments`: The output and input arguments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/context/executefunction(_:arguments:)-52eh3)*