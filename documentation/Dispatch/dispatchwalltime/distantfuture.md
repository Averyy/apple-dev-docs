# distantFuture

**Framework**: Dispatch  
**Kind**: property

A time in the distant future.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static let distantFuture: DispatchWallTime
```

#### Discussion

You can pass this value to methods that schedule work to have the system wait indefinitely for a particular event to occur or condition to be met.

## See Also

- [static func now() -> DispatchWallTime](dispatchwalltime/now.md)
  Returns the current time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchwalltime/distantfuture)*