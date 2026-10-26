# nw_parameters_set_privacy_context(_:_:)

**Framework**: Network  
**Kind**: func  
**Role**: Function

Associates a privacy context with any connections or listeners that use the parameters.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func nw_parameters_set_privacy_context(_ parameters: nw_parameters_t, _ privacy_context: nw_privacy_context_t)
```

```c
void nw_parameters_set_privacy_context(nw_parameters_t parameters, nw_privacy_context_t privacy_context);
```

## See Also

### Configuring Privacy Settings
- [typealias nw_privacy_context_t](./nw_privacy_context_t.md)
  An object that defines the privacy requirements for a set of connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/network/nw_parameters_set_privacy_context(_:_:))*