# isIsolatingCurrentContext()

**Framework**: Swift  
**Kind**: method  
**Required**: Yes

Checks if the current execution context is isolated by this executor.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
func isIsolatingCurrentContext() -> Bool?
```

#### Discussion

This function can be called by the runtime in order to perform assertions, or attempt to issue warnings about unexpected isolation.

This method will be invoked  `checkIsolated` and may also be invoked when crashing is not an acceptable outcome of a check (e.g. when attempting to issue isolation ).

Implementations should prefer to implement this method rather than `checkIsolated()` since it can often result in more tailored error messages. It is allowed, and useful for backwards compatibility with old runtimes which are not able to invoke `isIsolatingCurrentContext()` to implement `checkIsolated()`, even if an implementation is able to implement this method. Often times an implementation of `checkIsolated()`, would then invoke `isIsolatingCurrentContext()` and crash if the returned value was `false`.

The default implementation returns `nil` is used to indicate that it is “unknown” if the current context is isolated by this serial executor. The runtime then  proceed to invoke `checkIsolated()` as a last-resort attempt to verify the isolation of the current context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/serialexecutor/isisolatingcurrentcontext())*