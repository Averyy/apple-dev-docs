# removeDependency(_:)

**Framework**: Foundation  
**Kind**: method

Removes the receiver’s dependence on the specified operation.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func removeDependency(_ op: Operation)
```

#### Discussion

This method may change the `isReady` and `dependencies` properties of the receiver.

## Parameters

- `op`: The dependent operation to be removed from the receiver.

## See Also

- [func addDependency(Operation)](operation/adddependency(_:).md)
  Makes the receiver dependent on the completion of the specified operation.
- [var dependencies: [Operation]](operation/dependencies.md)
  An array of the operation objects that must finish executing before the current object can begin executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/removedependency(_:))*