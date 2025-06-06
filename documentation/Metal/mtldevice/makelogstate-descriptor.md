# makeLogState(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a shader log state with the provided configuration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func makeLogState(descriptor: MTLLogStateDescriptor) throws -> any MTLLogState
```

#### Return Value

A new [`MTLLogState`](mtllogstate.md) instance if the method completes successfully; otherwise Swift throws an error and Objective-C returns `nil`.

## Parameters

- `descriptor`: The configuration for the new shader log state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makelogstate(descriptor:))*