# dependencies

**Framework**: Foundation  
**Kind**: property

An array of the operation objects that must finish executing before the current object can begin executing.

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
var dependencies: [Operation] { get }
```

#### Discussion

This property contains an array of `NSOperation` objects. To add an object to this array, use the [`addDependency(_:)`](operation/adddependency(_:).md) method.

An operation object must not execute until all of its dependent operations finish executing. Operations are not removed from this dependency list as they finish executing. You can use this list to track all dependent operations, including those that have already finished executing. The only way to remove an operation from this list is to use the [`removeDependency(_:)`](operation/removedependency(_:).md) method.

## See Also

- [func addDependency(Operation)](operation/adddependency(_:).md)
  Makes the receiver dependent on the completion of the specified operation.
- [func removeDependency(Operation)](operation/removedependency(_:).md)
  Removes the receiver’s dependence on the specified operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/operation/dependencies)*