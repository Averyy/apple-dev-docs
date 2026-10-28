# ExecutionStatus

**Framework**: CarKey  
**Kind**: struct  
**Role**: Structure

A type that contains the status code a vehicle returns after executing an action.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.3+
- watchOS 9.0+

## Declaration

```swift
struct ExecutionStatus
```

## Overview

An [`ExecutionStatus`](./executionstatus.md) type wraps a code that indicates how your vehicle responded to a particular request. The Car Connectivity Consortium specifications define the meaning of most execution status codes, but you can define custom codes as needed for your vehicles.

## Topics

### Creating the Execution Status
- [init(rawValue: Int)](./executionstatus/init%28rawvalue%29.md)
  Creates and returns a new execution status with the specified value.
- [init(Int)](./executionstatus/init%28_%29.md)
  Creates and returns a new execution status with the specified value.
### Getting the Value
- [let rawValue: Int](./executionstatus/rawvalue.md)
  The raw value that corresponds to the feature-specific status.

## Relationships

### Conforms To
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting the Vehicle’s Response
- [func results() async throws -> ExecutionStatus](./remotekeylessentryaction/executionrequest/results%28%29.md)
  Returns the results of a preceding action request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carkey/executionstatus)*