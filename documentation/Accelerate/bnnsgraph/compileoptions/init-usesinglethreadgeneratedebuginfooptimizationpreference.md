# init(useSingleThread:generateDebugInfo:optimizationPreference:)

**Framework**: Accelerate  
**Kind**: init

Creates an allocated compilation-options object with the specified values.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS ?+
- watchOS 11.0+

## Declaration

```swift
init(useSingleThread: Bool = false, generateDebugInfo: Bool = false, optimizationPreference: BNNSGraph.CompileOptions.OptimizationPreference = .performance)
```

## Parameters

- `useSingleThread`: A Boolean value that specifies whether the graph executes on one thread.
- `generateDebugInfo`: A Boolean value that specifies whether the generated graph includes debug info.
- `optimizationPreference`: A constant that specifies the graph compilation-optimization preferences.

## See Also

- [init()](bnnsgraph/compileoptions/init.md)
  Creates an allocated compilation-options object with default values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsgraph/compileoptions/init(usesinglethread:generatedebuginfo:optimizationpreference:))*